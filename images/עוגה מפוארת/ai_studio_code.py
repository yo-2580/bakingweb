import os

# --- אזהרה ---
# סקריפט זה ישנה באופן קבוע את שמות הקבצים בתיקייה שבה הוא יופעל.
# מומלץ מאוד לגבות את הקבצים או להריץ אותו על עותק של התיקייה קודם כל!

def rename_files_in_current_directory():
    """
    סקריפט זה ממספר מחדש את כל הקבצים בתיקייה הנוכחית.
    המספור הוא בסדר עולה (0001, 0002, ...) לפי סדר אלפביתי של שמות הקבצים המקוריים.
    הסקריפט מתעלם מתיקיות ולא משנה את שם קובץ הסקריפט עצמו.
    """
    try:
        # קבלת הנתיב של התיקייה הנוכחית
        current_path = os.getcwd()
        print(f"מתחיל למספר קבצים בתיקייה: {current_path}")

        # קבלת שם הסקריפט הנוכחי כדי להימנע מלשנות אותו
        script_name = os.path.basename(__file__)

        # יצירת רשימה של כל הפריטים בתיקייה
        all_items = os.listdir(current_path)

        # סינון הרשימה כדי לכלול רק קבצים (ולא תיקיות או את הסקריפט עצמו)
        files_to_rename = [f for f in all_items if os.path.isfile(os.path.join(current_path, f)) and f != script_name]

        # מיון הקבצים לפי סדר אלפביתי (A-Z)
        files_to_rename.sort()
        
        if not files_to_rename:
            print("לא נמצאו קבצים לשינוי שם (מלבד הסקריפט עצמו).")
            return

        # הגדרת מונה שיתחיל מ-1
        counter = 1
        
        # חישוב מספר הספרות הנדרש (למשל, 4 ספרות עבור 0001)
        # זה מבטיח שאם יש יותר מ-9999 קבצים, הפורמט יישמר (למשל, 09999)
        padding = len(str(len(files_to_rename)))
        if padding < 4:
            padding = 4

        # לולאה שעוברת על כל הקבצים שסוננו
        for old_filename in files_to_rename:
            # פיצול שם הקובץ לשם ולסיומת
            # לדוגמה: "my_photo.jpg" -> ("my_photo", ".jpg")
            file_extension = os.path.splitext(old_filename)[1]

            # יצירת השם החדש עם מספר וסיומת
            # הפורמט f"{counter:0{padding}d}" יוצר מספר עם אפסים מובילים
            # לדוגמה, אם padding=4 ו-counter=1, התוצאה תהיה "0001"
            new_filename = f"{counter:0{padding}d}{file_extension}"

            # נתיב מלא לקובץ הישן והחדש
            old_filepath = os.path.join(current_path, old_filename)
            new_filepath = os.path.join(current_path, new_filename)

            # הדפסת הפעולה למסך
            print(f"משנה שם: '{old_filename}' -> '{new_filename}'")
            
            # ביצוע שינוי השם
            os.rename(old_filepath, new_filepath)
            
            # קידום המונה לקובץ הבא
            counter += 1

        print("\nהתהליך הסתיים בהצלחה!")

    except Exception as e:
        print(f"\nאירעה שגיאה: {e}")
        print("התהליך הופסק. ייתכן שחלק מהקבצים שונו וחלק לא.")

# הרצת הפונקציה הראשית
if __name__ == "__main__":
    # בקשת אישור מהמשתמש לפני ההרצה
    confirm = input("האם אתה בטוח שברצונך לשנות את שמות כל הקבצים בתיקייה זו? (כן/לא): ")
    if confirm.lower() == 'כן':
        rename_files_in_current_directory()
    else:
        print("הפעולה בוטלה.")
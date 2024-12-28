from app import app, db
from app.models import Search

def clean_duplicates():
    with app.app_context():
        unique_searches = set()
        duplicates = []
        for search in Search.query.all():
            identifier = (search.class_number, search.user_email)
            if identifier in unique_searches:
                duplicates.append(search)
            else:
                unique_searches.add(identifier)
        
        for duplicate in duplicates:
            db.session.delete(duplicate)
        
        db.session.commit()

if __name__ == "__main__":
    clean_duplicates()

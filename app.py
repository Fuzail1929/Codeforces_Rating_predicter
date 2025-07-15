from flask import Flask

app = Flask(__name__)

# Define your rating color dictionary at module level
RATING_COLORS = {
    "Newbie": "#A9A9A9",  # Gray
    "Pupil": "#32CD32",  # Lime Green
    "Specialist": "#00ffcc",  # Light Blue-Green
    "Expert": "#1E90FF",  # Dodger Blue
    "Candidate Master": "#800080",  # Purple
    "Master": "#FFD700",  # Gold
    "International Master": "#DAA520",  # Goldenrod
    "Grandmaster": "#DAA520",  # Same as International Master - is this correct?
    "International Grandmaster": "#DC143C",  # Crimson
    "Legendary Grandmaster": "#FF0000",  # Red
    "Tourist": "#FFFFFF"
}

DEFAULT_COLOR = "#A9A9A9"  # Gray

@app.route('/get/<string:s>', methods=['GET'])
def get(s):
    try:
        # Assuming func() processes the input and returns a tuple
        # (success_flag, (predicted_rating, user_data_dict))
        tup = func(s)  # func needs to be defined elsewhere
        
        if not tup[0]:  # If not successful
            return {'': ''}
        
        predicted_rating, user_data = tup[1]
        
        # Set rank color
        user_data['rank_color'] = RATING_COLORS.get(
            user_data.get('rank', '').title(), 
            DEFAULT_COLOR
        )
        
        # Set default rating if missing
        user_data.setdefault('rating', 0)
        
        # Determine message
        try:
            msg = ("You are above your Expected Rating, Bravo!!!" 
                  if predicted_rating > user_data['rating'] 
                  else "Hopefully, you will reach your expected rating soon :)")
        except (KeyError, TypeError):
            msg = "Hopefully, you will reach your expected rating soon :)"
        
        return {
            'user_data': user_data,
            'prediction': predicted_rating,
            'message': msg  # Consider adding the message to response
        }
        
    except Exception as e:
        # Better error handling - in production, you might want to log this
        return {'error': str(e)}, 500

if __name__ == '__main__':
    app.run(debug=True)

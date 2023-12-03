

from flask import Flask, request, jsonify
from flask_cors import CORS
from views import views
from recognition import prepare_refernce_faces
from recognition import recognition 
# ,create_faceEncodings_with_names,get_attendance,students_status

# from recognition import process_uploaded_image  # Import the necessary function from recognition.py

prepare_refernce_faces()
recognition()

app = Flask(__name__)
CORS(app)

app.register_blueprint(views, url_prefix="/")



if __name__ == "__main__":
    app.run(debug=True, port=5000)










# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from recognition import recognition, prepare_refernce_faces

# app = Flask(__name__)
# CORS(app)

# # ... Other code and configurations ...

# @app.route('/postdata', methods=['POST'])
# def handle_uploaded_data():
#     if request.method == 'POST':
#         uploaded_image = request.json.get('taken_imgs')  

#         # Pass the uploaded image to the recognition function
#         attendance_data = recognition(uploaded_image)

#         # Return the processed attendance data as a JSON response
#         return jsonify(attendance_data)

# # ... Other code ...

# if __name__ == "__main__":
#     prepare_refernce_faces()  # Prepare reference faces when the server starts
#     app.run(debug=True, port=5000)





















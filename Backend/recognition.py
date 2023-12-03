import face_recognition
import os
from utils import encode_npImage_to_base64

path_references = "References/level4"
path_takens = "img/taken img"
known_face_encodings = []
known_face_names = []


def prepare_refernce_faces():
    # Prepare Students faces for recognition
    create_faceEncodings_with_names(
        known_face_encodings, known_face_names, path_references
    )
    


# getting attendance
def recognition():
    attendance = {}

    for filename in os.listdir(path_takens):
        f = os.path.join(path_takens, filename)
        if os.path.isfile(f):
            # prepare the taken image for recognition
            taken_image = face_recognition.load_image_file(f)

            # Find faces in taken image
            face_locations = face_recognition.face_locations(
                taken_image, number_of_times_to_upsample=0, model="cnn"
            )
            print(f"Number of faces detected: {len(face_locations)}")

            face_encodings = face_recognition.face_encodings(
                taken_image, face_locations, model="large"
            )

            # Compare refernce faces with faces from the taken image and get the attendance faces and names
            get_attendance(
                face_locations,
                face_encodings,
                known_face_encodings,
                known_face_names,
                taken_image,
                attendance,
            )

    return students_status(path_references, attendance)


# prepare refernce faces for recognition
def create_faceEncodings_with_names(known_face_encodings, known_face_names, path):
    # iterate over the files in the folder to get images paths
    for filename in os.listdir(path):
        f = os.path.join(path, filename)
        if os.path.isfile(f):
            # prepare refernce face
            reference_face = face_recognition.load_image_file(f)
            student_face_encoding = face_recognition.face_encodings(
                reference_face, model="large"
            )[0]
            known_face_encodings.append(student_face_encoding)
            # getting the name from the filename then appending it to known_face_names
            
            known_face_names.append(filename.replace(".jpg", ""))



# Compare refernce faces with faces from the taken image and get the attendance faces and names
def get_attendance(
    face_locations,
    face_encodings,
    known_face_encodings,
    known_face_names,
    class_image,
    attendance,
):
    for face_location, face_encoding in zip(face_locations, face_encodings):
        # getting face location
        top, right, bottom, left = face_location
        # checking for the mathed faces
        matches = face_recognition.compare_faces(
            known_face_encodings, face_encoding, tolerance=0.5
        )
        # print(f"Matches: {matches}")
        # print(f"Face encoding: {face_encoding}")
        name = "Unknwon Person"

        # If match
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        if name != "Unknwon Person" and name not in attendance:
            # pull face
            face_image = class_image[top:bottom, left:right]
            # incode face to base64
            face_b64 = encode_npImage_to_base64(face_image)
            # appending face with name to the attendance data
            attendance[f"{name}"] = f"{face_b64}"


def students_status(r_face_path, attendance):
    all_students = []
    final_data = {"attendanceList": []}
    for filename in os.listdir(r_face_path):
        f = os.path.join(r_face_path, filename)
        if os.path.isfile(f):
            all_students.append(filename.replace(".jpg", ""))

    for student_attended in attendance:
        final_data["attendanceList"].append(
            {
                "snapshot": f"{attendance[student_attended]}",
                "studentId": student_attended,
                "status": "true",
            }
        )

    for student in all_students:
        if student not in attendance:
            final_data["attendanceList"].append(
                {"snapshot": "", "studentId": student, "status": "false"}
            )
            # print(f"final data: {final_data}")
    return final_data

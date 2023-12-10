async function uploadImage() {
    var input = document.getElementById('imageInput');


    if (input.files.length > 0) {
        var file = input.files[0];
        var reader = new FileReader();

        reader.onload = async function(e) {

            var base64 = e.target.result.split(',')[1];




            const data = {
                taken_imgs: {
                    image: base64,
                    // Add more images as needed
                },
            };

            // debugger;

            try {
                // Send the base64 data to the server asynchronously
                const response = await fetch('http://127.0.0.1:5000/postdata', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data),
                });

                if (!response.ok) {
                    console.error('Server returned an error:', response.statusText);
                    // Handle the error as needed
                    return;
                }
                const result = await response.json();
                console.log('Received data:', result);
                debugger;
                // Display the response
                displayTables(result.attendanceList);

            } catch (error) {
                console.error('Error:', error);
                document.getElementById('responseContainer').innerHTML = '<p>Error occurred. Check console for details.</p>';
            }
        };

        reader.readAsDataURL(file);
    } else {
        alert('Please select an image to upload.');
    }
}

function displayTables(attendanceList) {

    const attendedBody = document.getElementById('attendedBody');
    const absentBody = document.getElementById('absentBody');

    attendedBody.innerHTML = '';
    absentBody.innerHTML = '';



    attendanceList.forEach(student => {
        const snapshot = student.snapshot.slice(2, -1);
        const studentName = student.studentId;
        const status = student.status;

        const rowAttended = `<tr>
                        <td><img src="data:image/jpeg;base64,${snapshot}" alt="Snapshot" style="max-width: 100px; max-height: 100px;"></td>
                        <td>${studentName}</td>
                    </tr>`;


        const rowAbsence = `<tr>
                        <td>${studentName}</td>
                    </tr>`;
        if (status == 'true') {
            attendedBody.innerHTML += rowAttended;
        } else {
            absentBody.innerHTML += rowAbsence;
        }
    });
}
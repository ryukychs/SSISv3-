function deleteCollege(button) {
    console.log("Delete button clicked.");
    var college_code = button.getAttribute('college-code');
    var csrfToken = button.getAttribute('csrf-token');
    if (confirm("Are you sure you want to delete this college?\nStudents and Courses under this College will also be deleted.")) {
        fetch(`/colleges/delete/${college_code}`, {  
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrfToken
            }
        }).then(response => response.json())
        .then(data => {
            if (data.success === true) {
                window.location.reload();
            } else {
                console.error("Error: " + data.error);
            }
        });        
    }
}

function delCourse(button) {
    console.log("Delete button clicked.");
    var coursecode = button.getAttribute('course-code');
    var csrfToken = button.getAttribute('csrf-token');
    if (confirm("Are you sure you want to delete this course?")) {
        fetch(`/course/delete/${coursecode}`, {  
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrfToken
            }
        }).then(response => response.json())
        .then(data => {
            if (data.success === true) {
                window.location.reload();
            } else {
                console.error("Error: " + data.error);
            }
        });        
    }
}

function deleteStudent(button) {
    console.log("Delete button clicked.");
    var student_id = button.getAttribute('student-id');
    var csrfToken = button.getAttribute('csrf-token');
    if (confirm("Are you sure you want to delete this student?")) {
        fetch(`/students/delete/${student_id}`, {  // Fix the URL string
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrfToken
            }
        }).then(response => response.json())
        .then(data => {
            if (data.success === true) {
                window.location.reload();
            } else {
                console.error("Error: " + data.error);
            }
        });
    }
}


const searchInput = document.querySelector('.search-bar');
const collegeTable = document.getElementById('table');
const rows = collegeTable.getElementsByTagName('tr');

searchInput.addEventListener('input', function () {
    const searchTerm = this.value.trim().toLowerCase();

    for (let i = 1; i < rows.length; i++) {
        const row = rows[i];
        const cells = row.getElementsByTagName('td');
        let found = false; // Initialize found flag for the row

        for (let j = 0; j < cells.length; j++) {
            const cellText = cells[j].textContent.toLowerCase();

            if (cellText.includes(searchTerm)) {
                found = true; // Set the found flag
                break; // No need to check other cells in this row
            }
        }

        if (found) {
            row.style.display = ''; // Show the row
        } else {
            row.style.display = 'none'; // Hide the row
        }
    }
});


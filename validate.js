// static/js/validate.js
function validateForm() {
    const name = document.getElementById('name').value;
    const dob = document.getElementById('dob').value;
    const dod = document.getElementById('dod').value;
    const content = document.getElementById('content').value;
    const author = document.getElementById('author').value;

    if (!name || !dob || !dod || !content || !author) {
        alert('All fields are required.');
        return false;
    }

    const dobDate = new Date(dob);
    const dodDate = new Date(dod);
    if (dobDate >= dodDate) {
        alert('Date of Death must be after Date of Birth.');
        return false;
    }

    return true;
}

function sendMail(contactForm) {
    emailjs.send("gmail", "restaurant-contact", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "project_request": contactForm.messagecontent.value
    })
    .then(
        function(response) {
            console.log("Success", response);
        },
        function(error) {
            console.log("Failed", error);
        }
    );
    return false;
}
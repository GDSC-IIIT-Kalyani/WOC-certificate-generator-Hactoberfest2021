
document.querySelector(".contact-form").addEventListener("submit", submitForm);


function submitForm(e) {
    e.preventDefault();

    let uname = document.querySelector("#Name").value;
    let regno = document.querySelector("#RegNo").value;
    let rollno = document.querySelector("#RollNo").value;
    let email = document.querySelector("#Email").value;

    sendEmail(uname, regno, rollno, email);
}

function sendEmail(uname, regno, rollno, email)
{
    var Body = "Name : " + uname + "<br>Roll no : " + rollno + "<br>Reg no : " + regno + "<br>Here is your certificate.<br>";    
    
    Email.send({
            SecureToken : "9cf21f77-8627-48e4-87d1-5965f1d118c9",
            To : email,
            From : "adithyavenkat2310@gmail.com",
            Subject : "Certificate of completion.",
            Body : Body,
            // name of file 
            // address of file
            Attachments : [{
                name : "certificate.png",
                path : "https://media.istockphoto.com/vectors/elegant-blue-and-gold-diploma-certificate-template-vector-id1128426035"
            }],
        }).then(
            message => {
            alert("Thank you. your email has been send");
            });
}

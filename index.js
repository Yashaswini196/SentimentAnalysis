function submitForm(event) {
  event.preventDefault(); 
  var myInput  = document.getElementById("userinput").value;
  var data = {"emotionname": myInput, "id": 1};
  $.ajax({
    url: "http://localhost:8000/emotions/",
    type: "POST",
    data: JSON.stringify(data),
    contentType: "application/json",
    dataType: "json",
    success: function(response) {
      console.log(response['result']);
      var resultBox = document.getElementById("textresult");
      var message = "This is the required feeling: " + "</b>" + myInput + "</b>";
      resultBox.innerHTML = message;
      document.getElementById("result").innerHTML  = response.result;

    },
    error: function(error) {
      console.log(error);
    }
  });
}
var myForm = document.getElementById("myForm");
myForm.addEventListener("submit", submitForm);

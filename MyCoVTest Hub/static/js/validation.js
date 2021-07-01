$(document).ready(function(){

$("#email").keyup(function(){
    if(validateEmail()){
      $("#email").css("border","2px solid green");
      $("#emailMsg").html("<p class='text-success'>Validated</p>");
    }else{
      $("#email").css("border","2px solid red");
      $("#emailMsg").html("<p class='text-danger'>Un-validated</p>");
    }
    
  });

  $("#fullname").keyup(function(){
    var fnm = $("#fullname").val();
    var regnm = /^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/;
    var reg = reg =/^[0-9]+$/;
    if(fnm.length >0 && fnm.length<=3){
      $("#fullname").css("border", "2px solid red");
      $("#fnmMsg").html("<p class='text-danger'>Very Short Full Name!</p>");
    }
    else if (reg.test(fnm)){
      $("#fullname").css("border", "2px solid red");
      $("#fnmMsg").html("<p class='text-danger'>Name can not start with number!</p>");
    }
    else if(regnm.test(fnm)) {
      $("#fullname").css("border", "2px solid green");
     $("#fnmMsg").html("<p class='text-success'>Valid Name</p>");
    }
  });

  $("#age").keyup(function(){

    if($("#age").val()<18){
      $("#age").css("border", "2px solid red");
     $("#ageMsg").html("<p class='text-danger'>Only valid age allowed upto 19-99..!</p>");
    }else if($("#age").val()>18 && $("#age").val()<100) {
       $("#age").css("border", "2px solid green");
      $("#ageMsg").html("<p class='text-success'>Valid Age...!</p>");
    }
    else {
      $("#age").css("border", "2px solid red");
     $("#ageMsg").html("<p class='text-danger'>Invalid age...!!!</p>");
   }
  });


  $("#postcode").keyup(function(){

    var pc = $("#postcode").val();
    

  });
  // use keyup event on password

  $("#pwd").keyup(function(){
    // check
    if(validatePassword()){
      
      $("#pwd").css("border","2px solid green");
      //set passMsg
      $("#passMsg").html("<p class='text-success'>Password validated</p>");
    }else{
        // set input password border red
      $("#pwd").css("border","2px solid red");
      //set passMsg
      $("#passMsg").html("<p class='text-danger'>Password regired...<br>1. A minimum of 8 digit <br>2. At least one Upper case latter <br>3. At least one Lower case latter <br>4. At least one number</p>");
    }
    buttonState();
  });

  $("#cpwd").keyup(function(){

    if($("#pwd").val()==$("#cpwd").val()){
      $("#cpwd").css("border", "2px solid green");
     $("#cpassMsg").html("<p class='text-success'>Matched with password..!!</p>");
    }else {
       $("#cpwd").css("border", "2px solid red");
      $("#cpassMsg").html("<p class='text-danger'>Confirm password mismatch with password entered...!</p>");
    }

  });


});

function validateEmail(){
  // get value of input email
  var email=$("#email").val();
  // use reular expression
   var reg = /^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/
   if(reg.test(email)){
     return true;
   }else{
     return false;
   }
}

function validatePassword(){
  //get input password value
  var pass=$("#pwd").val();
  // check it s length
  var reg =/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/
  if(reg.test(pass)){
    return true;
  }else{
    return false;
  }

}



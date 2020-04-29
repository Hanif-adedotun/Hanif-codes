
	var divs = new Array();

	divs[0] = "errcloth";

	divs[1] = "errname";

	divs[2] = "erraddress";

	divs[3] = "erremail";

	divs[4] = "errquantity";

	divs[5] = "errnumber";
	
	divs[6] = "errFinal";

	function validate()

	{

	     var inputs = new Array();

	     inputs[0] = document.getElementById('cloth').value;

	     inputs[1] = document.getElementById('name').value;

	     inputs[2] = document.getElementById('address').value;

	     inputs[3] = document.getElementById('E-mail').value;

	     inputs[4] = document.getElementById('Quantity').value;

	     inputs[5] = document.getElementById('number').value;

	      var errors = new Array();

	     errors[0] = "<span style='color:red'>Please enter the name of the cloth!</span>";

	     errors[1] = "<span style='color:red'>Please enter your full name!</span>";

	     errors[2] = "<span style='color:red'>Please enter your house address!</span>";

	     errors[3] = "<span style='color:red'>Please enter your E-mail address!</span>";

	     errors[4] = "<span style='color:red'>Please enter the quantity!</span>";

	     errors[5] = "<span style='color:red'>Please enter your phone number!</span>";

	     for (i in inputs)

	     {

	          var errMessage = errors[i];

	          var div = divs[i];

	 

	          if (inputs[i] == "")

	              document.getElementById(div).innerHTML = errMessage;

	          else if (i==3)

	          {

	              var atpos=inputs[i].indexOf("@");

	              var dotpos=inputs[i].lastIndexOf(".");

	              if (atpos<1 || dotpos<atpos+2 || dotpos+2>=inputs[i].length)

	                  document.getElementById('erremail').innerHTML = "<span style='color: red'>Enter a valid email address!</span>";

	            else

	                  document.getElementById(div).innerHTML = "OK!";

	          }

	    else if (i==5)

	          {

	              var num = document.getElementById('number').value;
	              var tomatch = /^\d{11}$/;

	              if (tomatch.test(num))

	                   document.getElementById('errnumber').innerHTML = "OK!";
                       
	              else

	                   document.getElementById(div).innerHTML = "<span style='color: red'>Your phone number is wrong!</span>";

	          }

	        else

	              document.getElementById(div).innerHTML = "OK!";

	     }

	}

	function finalValidate()

	{

	     var count = 0;

	    for(i=0;i<6;i++)

	    {

	      var div = divs[i];

	      if(document.getElementById(div).innerHTML == "OK!")

	           count = count + 1;

	    }

	   if(count == 6)

	     document.getElementById("errFinal").innerHTML = "All the data you entered is correct!!!";

	}
	 
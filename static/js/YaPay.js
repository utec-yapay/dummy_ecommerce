$("#popupBoxOnePosition").hide();
$("#qr").attr("src", "/static/images/loading.gif");

function toggle_visibility(id) {
    if($("#yape").prop("checked")){
        if ($(id).is(":hidden")){
            console.log("Showing QR");
            setQr("#qr");
        }

        $(id).fadeToggle("fast");
    } 
 }


 function setQr(id){
     var data = {
         "amount": 100,
         "companyName": "drimer",
         "companyPhone": "993321323",
     };

     data = JSON.stringify(data)

     $.ajax({
      type: "POST",
      url: "http://localhost:8080/payments",
      data: data,
      contentType: "application/json"
    })
     .success(function(response) {
         $("#qr").attr("src", response["qrData"]);
     })
     .fail(function(error) { alert(JSON.stringify(error))});

}


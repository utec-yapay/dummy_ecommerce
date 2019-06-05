function toggle_visibility(id) {
    if(document.getElementById("yape").checked){
        var e = document.getElementById(id);
        if(e.style.display == 'block')
            e.style.display = 'none';
        else
            e.style.display = 'block';
    }
 }
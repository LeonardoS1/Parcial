function required(){
    event.preventDefault();
    var nombre= document.getElementById("txtNombre").value;
    var email= document.getElementById("txtEmail").value;
    var apellidos= document.getElementById("txtApellidos").value;
    var direccion= document.getElementById("txtDireccion").value;
    var telefono= document.getElementById("txtTelefono").value;
    var pattern = /^\b[a-z0-9._%-]+@[a-z0-9.-]+\.[a-z]{2,4}\b$/i 
    var comunas= document.getElementById("comunas").value;
    var regiones= document.getElementById("regiones").value;
    
    document.getElementById("ptxtNombre").hidden=true
    document.getElementById("ptxtApellidos").hidden=true
    document.getElementById("ptxtEmail").hidden=true
    document.getElementById("ptxtDireccion").hidden=true
    document.getElementById("ptxtTelefono").hidden=true
    document.getElementById("ptxtComunas").hidden=true
    document.getElementById("ptxtRegiones").hidden=true

   if(nombre==""){
        document.getElementById("ptxtNombre").hidden=false
        document.getElementById("ptxtNombre").innerHTML = "El nombre no puede quedar vacío";
        //alert("El nombre no puede quedar vacío")
       return false;
    }

    if(apellidos==""){
        document.getElementById("ptxtApellidos").hidden=false
        document.getElementById("ptxtApellidos").innerHTML = "Los apellidos no puede quedar vacío";
        //alert("Los apellidos no puede quedar vacío")
       return false;
    }

    if(email==""){
        document.getElementById("ptxtEmail").hidden=false
        document.getElementById("ptxtEmail").innerHTML = "El email no puede quedar vacío";
        //alert("El email no puede quedar vacío")
       return false;
    }
        
    if(!pattern.test(email)){
        document.getElementById("ptxtEmail").hidden=false
        document.getElementById("ptxtEmail").innerHTML = "El email debe contener un arroba";
        //alert('Ingrese un email válido')
        return false;
    }

    if(direccion==""){
        document.getElementById("ptxtDireccion").hidden=false
        document.getElementById("ptxtDireccion").innerHTML = "La dirección  no puede quedar vacío";
        //alert("La dirección no puede quedar vacío")
       return false;
    }
    if(telefono.length!=9){
        document.getElementById("ptxtTelefono").hidden=false
        document.getElementById("ptxtTelefono").innerHTML = "El teléfono no puede quedar vacío";
        //alert("El número de telefono tiene que tener nueve dígito")
       return false;
    }

    if(regiones=="sin-region"){
        document.getElementById("ptxtRegiones").hidden=false
        document.getElementById("ptxtRegiones").innerHTML = "Debe seleccionar una región";  
        return false;
    }

    if(comunas=="sin-region" || comunas=="sin-comuna"){
        document.getElementById("ptxtComunas").hidden=false
        document.getElementById("ptxtComunas").innerHTML = "Debe seleccionar una comuna";  
        return false;
    }

    

}

document.addEventListener("DOMContentLoaded", function() {
    //document.getElementById("formulario").addEventListener('submit', validarFormulario); 
});
function validarFormulario(evento) {
    evento.preventDefault();
    var usuario = document.getElementById('usuario').value;
    if(usuario.length == 0) {
      alert('No has escrito nada en el usuario');
      return;
    }
    var password = document.getElementById('password').value;
    if (password.length < 6) {
      alert('La contraseña no es válida');
      return;
    }
    this.submit();
}

$("#crear_usuario").validate({
    "errorClass": "is-invalidate",
    "rules":{
        first_name:{
            required: true
        },
        last_name:{
            required: true
        },
        email:{
            required: true
        },
        username:{
            required: true,
            minlength: 3,
            maxlength: 15
        },
        password:{
            required: true,
            minlength: 8,
            maxlength: 15
        },
    },
    "messages":{
        first_name:{
            required: "El nombre es obligatorio"
        },
        last_name:{
            required: "El apellido es obligatorio"
        },
        email:{
            required: "El email es obligatorio"

        },
        username:{
            required: "El nombre de usuario es obligatorio",
            minlength: "El minimo de caracteres es de 3",
            maxlength: "El maximo de caracteres es de 15"
        },
        password:{
            required: "La contraseña es obligatoria",
            minlength: "El minimo de caracteres es de 8",
            maxlength: "El maximo de caracteres es de 15"
        }
    }
})


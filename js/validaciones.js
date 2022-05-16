function required(){
    var nombre= document.getElementById("txtNombre").value;
    var email= document.getElementById("txtEmail").value;
    var apellidos= document.getElementById("txtApellidos").value;
    var direccion= document.getElementById("txtDireccion").value;
    var telefono= document.getElementById("txtTelefono").value;
    var pattern = /^\b[a-z0-9._%-]+@[a-z0-9.-]+\.[a-z]{2,4}\b$/i 

   if(nombre==""){
        alert("El nombre no puede quedar vacío")
       return false;
    }

    if(apellidos==""){
        alert("Los apellidos no puede quedar vacío")
       return false;
    }

    if(email==""){
        alert("El email no puede quedar vacío")
       return false;
    }
        
    if(!pattern.test(email)){
        alert('Ingrese un email válido')
        return false;
    }

    if(direccion==""){
        alert("La dirección no puede quedar vacío")
       return false;
    }
    if(telefono.length!=9){
        alert("El número de telefono tiene que tener nueve dígito")
       return false;
    }

}

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("formulario").addEventListener('submit', validarFormulario); 
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


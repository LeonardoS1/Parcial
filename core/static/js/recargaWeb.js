const iFrameNosotros = '<iframe class="ifForm" src="Nosotros.html" scrolling="no" frameborder="0"></iframe>'
const iFrameTienda = '<iframe class="ifForm" src="Tienda.html" scrolling="no" frameborder="0"></iframe>'
const iFrameDonaciones = '<iframe class="ifForm" src="donaciones.html" scrolling="no" frameborder="0"></iframe>'
const iFrameContacto = '<iframe class="ifForm" src="{% url "contacto" %}" scrolling="no" frameborder="0"></iframe>'

const mostrarNosotros = ()=>{
    Carga.innerHTML=iFrameNosotros
}
const mostrarTienda = ()=>{
    Carga.innerHTML=iFrameTienda
}
const mostrarDonaciones = ()=>{
    Carga.innerHTML=iFrameDonaciones
}
const mostrarContacto = ()=>{
    Carga.innerHTML="<h1>completado</h1>"
}

// fetch('https://reqres.in/api/users?page=2')
//   .then(response => response.json())
//   .then(data => console.log(data));
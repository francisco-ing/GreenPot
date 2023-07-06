// MENU HAMBURGUESA

function menu() {
    var x = document.getElementById("myLinks");
    if (x.style.display === "block") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
    }
}

// VALIDACIONES PARA AGREGAR PRODUCTO

function validarCodProducto(){
    var codprd = document.querySelector("#codigo-producto");
    if(isNaN(codprd.value)){
        codprd.classList.add("error");
    }else{
        codprd.classList.remove("error");
    }
}

function validarNombreProducto(){
    var nomprd = document.querySelector("#nombre-producto");
    if(3 <= nomprd.value.length && nomprd.value.length <= 25){
        nomprd.classList.remove("error");
    }else{  
        nomprd.classList.add("error");
    }
}

function validarDescProducto(){
    var desc = document.querySelector("#desc-producto");
    if(1 <= desc.value.length && desc.value.length <= 50){
        desc.classList.remove("error");
    }else{  
        desc.classList.add("error");
    }
}

function validarPrecioProducto(){
    var prec = document.querySelector("#precio-producto");
    if(isNaN(prec.value)){
        prec.classList.add("error");
    }else{  
        prec.classList.remove("error");
    }
}

function validarStockProducto(){
    var stock = document.querySelector("#stock-producto");
    if(isNaN(stock.value)){
        stock.classList.add("error");
    }else{  
        stock.classList.remove("error");
    }
}

function validarProducto(){
    var codprd = document.querySelector("#codigo-producto");
    var nomprd = document.querySelector("#nombre-producto");
    var descprd = document.querySelector("#desc-producto");
    var precprd = document.querySelector("#precio-producto");
    var stockprd = document.querySelector("#stock-producto");

    if (codprd.classList.contains("error")){
        alert("Error en el campo codigo!.");
        return false;
    }

    if (nomprd.classList.contains("error")){
        alert("Error en el campo nombre producto!.");
        return false;
    }

    if (descprd.classList.contains("error")){
        alert("Error en el campo descripcion!.");
        return false;
    }

    if (precprd.classList.contains("error")){
        alert("Error en el campo precio!.");
        return false;
    }

    if (stockprd.classList.contains("error")){
        alert("Error en el campo stock!.");
        return false;
    }

    alert("Producto agregado con exito!.");
    return true; 
}


// VALIDACIONES PARA ELIMINAR PRODUCTO

function validarCodProductoEliminar(){
    var codprd = document.querySelector("#codigo-producto-el");
    if(isNaN(codprd.value)){
        codprd.classList.add("error");
    }else{
        codprd.classList.remove("error");
    }
}

function validarProductoEliminar(){
    var codprd = document.querySelector("#codigo-producto-el");

    if (codprd.classList.contains("error")){
        alert("Error en el campo codigo!.");
        return false;
    }

    alert("Producto eliminado con exito!.");
    return true; 
}


// VALIDACIONES PARA EDITAR PRODUCTO

function validarPrecioProductoEditar(){
    var prec = document.querySelector("#precio-producto-ed");
    if(isNaN(prec.value)){
        prec.classList.add("error");
    }else{  
        prec.classList.remove("error");
    }
}

function validarStockProductoEditar(){
    var stock = document.querySelector("#stock-producto-ed");
    if(isNaN(stock.value)){
        stock.classList.add("error");
    }else{  
        stock.classList.remove("error");
    }
}

function validarProductoEditar(){
    var precprd = document.querySelector("#precio-producto-ed");
    var stockprd = document.querySelector("#stock-producto-ed");

    if (precprd.classList.contains("error")){
        alert("Error en el campo precio!.");
        return false;
    }

    if (stockprd.classList.contains("error")){
        alert("Error en el campo stock!.");
        return false;
    }

    alert("Producto editado con exito!.");
    return true; 
}

// VALIDACIONES PARA NOMBRE DE USUARIO

function validarLogin(){
    var nomusr = document.querySelector("#nombre-usuario");
    var con = document.querySelector("#contrasenia");

    if (nomusr.classList.contains("error")){
        alert("Error en el campo nombre de usuario!.");
        return false;
    }

    if (con.classList.contains("error")){
        alert("Error en el campo contrasenia!.");
        return false;
    }

    location.href ="micuenta.html";
    alert("Login exitoso!.");
    return true; 
}

// VALIDACIONES PARA REGISTRO DE USUARIO

function validarNombreUsuario(){
    var nomusr = document.querySelector("#nombre-usuario");
    if(6 <= nomusr.value.length && nomusr.value.length <= 20){
        nomusr.classList.remove("error");
    }else{
        nomusr.classList.add("error");
    }
}

function validarContrasenia(){
    var con = document.querySelector("#contrasenia");
    if(6 <= con.value.length && con.value.length <= 15){
        con.classList.remove("error");
    }else{
        con.classList.add("error");
    }
}

function validarNombre(){
    var nom = document.querySelector("#nombre");
    if(10 <= nom.value.length && nom.value.length <= 25){
        nom.classList.remove("error");
    }else{  
        nom.classList.add("error");
    }
}

function validarCorreo(){
    var corr = document.querySelector("#correo");
    if(corr.value.includes("@") && corr.value.length >= 6){
        corr.classList.remove("error");
    }else{
        corr.classList.add("error");
    }
}

function validarForm() {
    var nomusr = document.querySelector("#nombre-usuario");
    var nom = document.querySelector("#nombre");
    var corr = document.querySelector("#correo");
    var con = document.querySelector("#contrasenia");
    var msj = document.getElementById("mensaje");

    if (nom.classList.contains("error")){
        alert("Error en el campo nombre!.");
        return false;
    }

    if (nomusr.classList.contains("error")){
        alert("Error en el campo nombre de usuario!.");
        return false;
    }

    if (corr.classList.contains("error")){
        alert("Error en el campo correo!.");
        return false;
    }

    if (con.classList.contains("error")){
        alert("Error en el campo contrasenia!.");
        return false;
    }


        
        location.href ="login.html";
        alert("Cuenta creada con exito!.");
        return true; 
}

// VALIDACIONES PARA ELIMINAR USUARIO
function validarCodUsrEliminar(){
    var corr = document.querySelector("#codigo-usr-el");
    if(2 <= corr.value.length && corr.value.length <= 4){
        corr.classList.remove("error");
    }else{
        corr.classList.add("error");
    }
}

function validarUsuarioEliminar(){
    var codusr = document.querySelector("#codigo-usr-el");

    if (codusr.classList.contains("error")){
        alert("Error en el campo codigo de usr!.");
        return false;
    }

    alert("Usuario eliminado con exito!.");
    return true; 
}

// VALIDACIONES PARA EDITAR USUARIO

function validarNombreUsuarioEditar(){
    var nomusr = document.querySelector("#nombre-usuario-ed");
    if(6 <= nomusr.value.length && nomusr.value.length <= 20){
        nomusr.classList.remove("error");
    }else{
        nomusr.classList.add("error");
    }
}

function validarCorreoEditar(){
    var corr = document.querySelector("#correo-ed");
    if(corr.value.includes("@") && corr.value.length >= 6){
        corr.classList.remove("error");
    }else{
        corr.classList.add("error");
    }
}

function validarNombreEditar(){
    var nom = document.querySelector("#nombre-ed");
    if(10 <= nom.value.length && nom.value.length <= 25){
        nom.classList.remove("error");
    }else{  
        nom.classList.add("error");
    }
}

function validarUsuarioEditar(){
    var nom = document.querySelector("#nombre-ed");
    var nomusr = document.querySelector("#nombre-usuario-ed");
    var corr = document.querySelector("#correo-ed");

    if (nom.classList.contains("error")){
        alert("Error en el campo nombre!.");
        return false;
    }

    if (nomusr.classList.contains("error")){
        alert("Error en el campo nombre de usuario!.");
        return false;
    }

    if (corr.classList.contains("error")){
        alert("Error en el campo correo!.");
        return false;
    }

    alert("Usuario editado con exito!.");
    return true; 
}

function borrar(){
    document.querySelector('#buscar').value = "";
}
// creamos la funcion
function validarFormulario(){
    // removemos el div con la clase alert
    $('.alert').remove();


    // declarion de variables
    var name=$('#name').val(),
        email=$('#email').val(),
        phone=$('#phone').val(),
        mesaje=$('#mesaje').val();

    // validamos el campo nombre
    if(name=="" || name==null){

        cambiarColor("name");
        // mostramos le mensaje de alerta
        mostraAlerta("Campo obligatorio");
        return false;
    }else{
        var expresion= /^[a-zA-ZñÑáéíóúÁÉÍÓÚ ]*$/;
        if(!expresion.test(name)){
            // mostrara el mesaje que debe ingresar un nombre válido
            cambiarColor("name");
            mostraAlerta("No se permiten carateres especiales o numeros");
            return false;
        }
    }

    // validamos el correo
    if(email=="" || email==null){

        cambiarColor("email");
        // mostramos le mensaje de alerta
        mostraAlerta("Campo obligatorio");
        return false;
    }else{
        var expresion= /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
        if(!expresion.test(email)){
            // mostrara el mesaje que debe ingresar un nombre válido
            cambiarColor("email");
            mostraAlerta("Por favor ingrese un correo válido");
            return false;
        }
    }

    // validamos el asunto
    if(phone=="" || phone==null){

        cambiarColor("phone");
        // mostramos le mensaje de alerta
        mostraAlerta("Campo obligatorio");
        return false;
    }else{
        var expresion= /^[,\\.\\a-zA-Z0-9ñÑáéíóúÁÉÍÓÚ ]*$/;
        if(!expresion.test(phone)){
            // mostrara el mesaje que debe ingresar un nombre válido
            cambiarColor("phone");
            mostraAlerta("No se permiten caracteres especiales");
            return false;
        }
    }

     // validamos el mensaje
     if(mesaje=="" || mesaje==null){

        cambiarColor("mesaje");
        // mostramos le mensaje de alerta
        mostraAlerta("Campo obligatorio");
        return false;
    }else{
        var expresion= /^[,\\.\\a-zA-Z0-9ñÑáéíóúÁÉÍÓÚ ]*$/;
        if(!expresion.test(mesaje)){
            // mostrara el mesaje que debe ingresar un nombre válido
            cambiarColor("mesaje");
            mostraAlerta("No se permiten caracteres especiales");
            return false;
        }
    }

    $('form').submit();
    return true;
    
} 

$('input').focus(function(){
    $('.alert').remove();
    colorDefault('name');
    colorDefault('email');
    colorDefault('phone');
});

$('textarea').focus(function(){
    $('.alert').remove();
    colorDefault('mesaje');
});

// creamos un funcion de color por defecto a los bordes de los inputs
function colorDefault(dato){
    $('#' + dato).css({
        border: "1px solid #999"
    });
}

// creamos una funcio para cambiar de color a su bordes de los input
function cambiarColor(dato){
    $('#' + dato).css({
        border: "1px solid #dd5144"
    });
}

// funcion para mostrar la alerta

function mostraAlerta(texto){
    $('#name').before('<div class="alert">Error: '+ texto +'</div>');
}

// const form = document.getElementById('form')
// const button = document.getElementById('submit')

// const name = document.getElementById('name')
// const email = document.getElementById('email')
// const phone = document.getElementById('phone')

// const formIsValid = {
//     name:false,
//     email:false,
//     phone:false,
// }

// form.addEventListener('submit', (e) => {
//        e.preventDefault
//        validateForm()
// })

// name.addEventListener('change', (e)=>{
//     if(e.target.value.trim().length > 0) formIsValid.name = true
// })

// name.addEventListener('change', (e)=>{
//     if(e.target.value.trim().length > 0) formIsValid.email = true
// })

// name.addEventListener('change', (e)=>{
//     if(e.target.value.trim().length > 0) formIsValid.phone = true
// })

// const validateForm = () => {
//     const formValues = Object.values(formIsValid)
//     const valid = formValues.findIndex(value => value == false)
//     if(valid == -1) form.submit()
//     else alert('Formulario Invalido')
// }
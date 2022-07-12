function inserir(numero){
    const num = document.getElementById('resultado').innerHTML
    document.getElementById('resultado').innerHTML = num + numero
}

function limpar(){
    document.getElementById('resultado').innerHTML = ""
}

function apagar(){
    const resultado = document.getElementById('resultado').innerHTML
    document.getElementById('resultado').innerHTML = resultado.substring(0, resultado.length -1)
}

function calcular()
        {
            const resultado = document.getElementById('resultado').innerHTML
            if(resultado){
                document.getElementById('resultado').innerHTML = eval(resultado)
            } else{
                document.getElementById('resultado').innerHTML = "Erro"
            }
        }

/* Formatação */



/* 
Teclado 

const mapeamento = {
    '0' : 'b1'
}
const mapear = (evento) => {
    const tecla = evento.key
    document.getElementById(mapeamento[tecla]).click()
}
document.addEventListener('keydown', mapear)
*/
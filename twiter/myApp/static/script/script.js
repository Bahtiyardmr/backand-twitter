    var Form1 = document.getElementById('Form1')
    var Form2 = document.getElementById('Form2')

    var Next = document.getElementById('Next')
    var Giris = document.getElementById('Giris')

    Next.onclick = function(){
        Form1.style.display ="none";
        Form2.style.display ='block'
    }
  
        var Form1 = document.getElementById('Form1')
        var Form2 = document.getElementById('Form2')
        var Form3 = document.getElementById('Form3')
        var Mobil = document.getElementById('mobil')
        var Email = document.getElementById('email')

        var Next = document.getElementById('Next')
        var Next2 = document.getElementById('Next2')
        var Next3 = document.getElementById('Next3')
        var Back = document.getElementById('Back')
        var Back2 = document.getElementById('Back2')
        var Back3 = document.getElementById('Back3')
        var Show = document.getElementById('show')
        var Show2 = document.getElementById('show2')

        Show.onclick=function(){
            Mobil.style.display='none';
            Email.style.display='block';
            Show.style.display='none';
            Show2.style.display='block';
        }
        Show2.onclick=function(){
            Mobil.style.display='block';
            Email.style.display='none';
            Show.style.display='block';
            Show2.style.display='none';
        }


        Next.onclick = function () {
            Form1.style.display = "none";
            Form2.style.display = 'block'

        }

        Next2.onclick = function () {
            Form1.style.display = "none";
            Form2.style.display = "none";
            Form3.style.display = "block";
        }

        Next3.onclick = function () {
            Form1.style.display = "none";
            Form2.style.display = "none";
            Form3.style.display = "none";
            Form4.style.display = "block";
        }
        Back.onclick = function () {
            Form1.style.display = "none";
            Form2.style.display = "block";
            Form3.style.display = "none";
        }
        Back2.onclick = function () {
            Form1.style.display = "none";
            Form2.style.display = "none";
            Form3.style.display = "block";
            Form4.style.display = "none";
        } 

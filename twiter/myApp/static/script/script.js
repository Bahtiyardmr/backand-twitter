 
        var Form1 = document.getElementById('Form1')
        var Form2 = document.getElementById('Form2')

        var Next = document.getElementById('Next')
        var Giris = document.getElementById('Giris')

        Next.onclick = function () {
            Form1.style.display = "none";
            Form2.style.display = 'block'
        }
 
  
        var Form1 = document.getElementById('Form1')
        var Form2 = document.getElementById('Form2')
        var Form3 = document.getElementById('Form3')
        var Form4 = document.getElementById('Form4')
        var Form5 = document.getElementById('Form5')

        var Next = document.getElementById('Next')
        var Next2 = document.getElementById('Next2')
        var Next3 = document.getElementById('Next3')
        var Next4 = document.getElementById('Next4')
        var Back = document.getElementById('Back')
        var Back2 = document.getElementById('Back2')
        var Back3 = document.getElementById('Back3')

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
        Next4.onclick = function () {
            Form1.style.display = "none";
            Form2.style.display = "none";
            Form3.style.display = "none";
            Form4.style.display = "none";
            Form5.style.display = "block";
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

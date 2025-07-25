
<html>
       
   
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Simple HTML HomePage</title>
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
      <style>
        @import url('https://fonts.googleapis.com/css2?family=Sriracha&display=swap');
        body {
          margin: 0;
          box-sizing: border-box;
        }
            

        /* CSS for header */
        .header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          background-color: #f5f5f5;
        }

        .header .logo {
          font-size: 25px;
          font-family: 'Sriracha', cursive;
          color: #000;
          text-decoration: none;
          margin-left: 30px;
        }

        .nav-items {
          display: flex;
          justify-content: space-around;
          align-items: center;
          background-color: #f5f5f5;
          margin-right: 20px;
        }


        .nav-items a {
          text-decoration: none;
          color: #000;
          padding: 35px 20px;
        }


        /* CSS for main element */
        .intro {
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
          width: 100%;
          height: 500px;
          background: linear-gradient(to bottom, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.5) 100%), url(https://images.unsplash.com/photo-1675789652617-d84e3d201ef4?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=871&q=80);
          background-size: cover;
          background-position: center;
          background-repeat: repeat;
        }

        .intro h1 {
          font-family: sans-serif;
          font-size: 60px;
          color: #fff;
          font-weight: bold;
          text-transform: uppercase;
          margin: 0;
        }

        .intro p {
          font-size: 20px;
          color: #d1d1d1;
          text-transform: uppercase;
          margin: 20px 0;
        }


        .intro button {
          background-color: #5edaf0;
          color: #000;
          padding: 10px 25px;
          border: none;
          border-radius: 5px;
          font-size: 20px;
          font-weight: bold;
          cursor: pointer;
          box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.4)
        }

        .achievements {
          display: flex;
          justify-content: space-around;
          align-items: center;
          padding: 40px 80px;
        }


        .achievements .work {
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
          padding: 0 40px;
        }

        .achievements .work i {
          width: fit-content;
          font-size: 50px;
          color: #333333;
          border-radius: 50%;
          border: 2px solid #333333;
          padding: 12px;
        }

        .achievements .work .work-heading {
          font-size: 20px;
          color: #333333;
          text-transform: uppercase;
          margin: 10px 0;
        }

        .achievements .work .work-text {
          font-size: 15px;
          color: #585858;
          margin: 10px 0;
        }

        .about-me {
          display: flex;
          justify-content: center;
          align-items: center;
          padding: 40px 80px;
          border-top: 2px solid #eeeeee;
        }

        .about-me img {
          width: 500px;
          max-width: 100%;
          height: auto;
          border-radius: 10px;
        }

        .about-me-text h2 {
          font-size: 30px;
          color: #333333;
          text-transform: uppercase;
          margin: 0;
        }

        .about-me-text p {
          font-size: 15px;
          color: #585858;
          margin: 10px 0;
        }

       /* CSS for footer */
        .footer {
          display: flex;
          justify-content: space-between;
          align-items: center;
          background-color: #302f49;
          padding: 40px 80px;
        }

        .footer .copy {
          color: #fff;
        }

        .bottom-links {
          display: flex;
          justify-content: space-around;
          align-items: center;
          padding: 40px 0;
        }

        .bottom-links .links {
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
          padding: 0 40px;
        }

        .bottom-links .links span {
          font-size: 20px;
          color: #fff;
          text-transform: uppercase;
          margin: 10px 0;
        }

        .bottom-links .links a {
          text-decoration: none;
          color: #a1a1a1;
          padding: 10px 20px;
        }

        .running-letter {
          animation: running-letter 5s linear infinite;
        }

        @keyframes running-letter {
        from {
        transform: translateX(100%);
        }
        to {
        transform: translateX(-200%);
        }
        }
      </style>
    </head>

     <body>
       <header class="header">
          <a href="#" class="logo">ARUNKUMAR</a>
          <p class="running-letter">Help Line:7994241228</p>

          
        </header>
        <main>
          <div class="intro">
            <h1>Weathertron</h1>
            <p>Weather and Fire Related services</p>


           </div>
           <div class="achievements">
              <div class="work">
                <i class="fas fa-fire"></i>
                <p class="work-heading">FOREST</p>
                <p class="work-text">"Green is the new gold, save our forests"</p>
              </div>
              <div class="work">
                <i class="fas fa-male"></i>
                <p class="work-heading">Responsibilities</p>
                <p class="work-text">Forest Conservation Act 1980
                             Protect the forest along with its flora, fauna and other diverse ecological components
              </div>
              <div class="work">
                <i class="fas fa-ethernet"></i>
                <p class="work-heading">Organizations</p>
                <p class=<ul>
                <li>Ministry of Environment</li>
                <li>Forest Survey Of India </li>

                </p>
              </div>
              </div>
              <div class="about-me">
                <div class="about-me-text">
                  <h2>About The Services We Providing</h2>
                  <p class=<ul>
                  <li> Weather</li>
                  <li> Fire Prediction</li>
                  <li> Preventing Techniques</li>
                  <li> Locating You</li>
                  You Can avail all services by Accessing the navigation bar
                  </p>
                </div>
                <img src="https://images.unsplash.com/photo-1605092676920-8ac5ae40c7c8?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=465&q=80 alt="me">
              </div>
            </main>
            <footer class="footer">
              <div class="copy">&copy; 2023 Final Project</div>
              <div class="bottom-links">
                <div class="links">
                  <span>More Info</span>
                  <a href="#">Me</a>
                  <a href="#">My Guide</a>
                  <a href="#">Contact</a>
                </div>
                <div class="links">
                  <span></span>
                  <a href="#">ARUNKUMAR V</a>
                  <a href="#">KANIMOZHI.V</a>
                  <a href="#">oyeahitsarun@gmail.com</a>
                  </div>
                </div>
              </footer>
            </body>
            </html>"""
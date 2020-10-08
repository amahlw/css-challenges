<!DOCTYPE html>
<html lang="en">

<head>
  <title>Challenge 5</title>
  <style>
    /* Style the weather report */

    /* Apply the following styles to the body */
    body{
      
   
      /* font family 'Helvetica Neue' */
      font-family: Arial, Helvetica, sans-serif;
      font-size:20px ;
      /* font size 20px */
      /* line height 1.5 */
      line-height: 1.5;
      /* Color #333 dark gray */
      color: #333;
      /* background color #eee light gray */
      background-color: #eee;
    }

    /* Style the dt (definition title) */
    dt{ 

    
      /* Make the font really big! 2em */
      font:larger;
      font: 2em;
      /* Make the background color light gray #ccc */
      background-color: #ccc;
      }
      

    /* Style the dd (definition) */
    dd{

   
      /* make the font big 1.5em */
      font: large;
      font: 1.5em;
      /* Background color #ddd */
      background-color: #ddd;
      /* Remove the by setting margin: 0 */
      margin: none;
    }


    /* Style both the dt and dd */
    
    /* Using the comma groups selectors */
    dt, dd {
      /* Add some space between these elements and their content */
      
      /* padding: 0.5em */
      padding: 0.5em;
      
    }

    /* Stretch Challenges: 
    
    - Adjust these styles to your taste. What do you think would 
    look best here? 
    - Edit the HTML, add a new list item with a new weather report. 
      - 06 March 2018 
      - Partially cloudy
      - 07 March 2018
      - Sunny and clear
    - Change the background color for each row. You want the rows to be 
    light blue with the two rows using a different shade of blue. 
    - Use text-align to move the heading text to the right. 

     */

  </style>
</head>

<body>

<article>
  <header>
    <h1>Weather forecast for Seattle</h1>
    <p>Three day forecast</p>
  </header>
  <dl>
    <dt><time datetime="2018-03-03">03 March 2018</time></dt>
    <dd>Rain.</dd>

    <dt><time datetime="2018-03-04">04 March 2018</time></dt>
    <dd>Periods of rain.</dd>

    <dt><time datetime="2018-03-05">05 March 2018</time></dt>
    <dd>Heavy rain.</dd>
  </dl>
</article>

</body>
</html>

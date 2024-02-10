# SkyScan - Reading between the clouds for you!

<img src="https://github.com/sathvik9105/amfoss-tasks/blob/main/task-07/images/logo.png?raw=true" alt="Logo" style="width: 250px;"/>

## What is SkyScan?

- <b>SkyScan</b> is a basic chrome extension that provides real-time weather data for an input location. 
- Users can view the current weather condition, actual-temperature, feelslike-temperature, info regarding the clouds for  any location (input as city name). - This mini-project has been developed using HTML, CSS, JavaScript, and integrates with the OpenWeatherMap API to fetch the weather data.


## How is SkyScan developed?

- **HTML:** The structure of the web page is defined in HTML. It includes containers for displaying weather information, an input field to enter any city name and a button to check the weather of the input city.

- **CSS:** The CSS file is used for styling the web page. It includes fonts, colors, background colors, layouts, images, etc. I have created a responsive design for the extension. 

- **JavaScript:** JavaScript is responsible for fetching weather data, handling user interactions, and dynamically updating the web page content.


## How does SkyScan work?
- <u>Weather data retrieval</u>: The extension uses OpenWeatherMap API to fetch weather data based on a city name entered by user.

- <u>Display weather</u>: The retrieved weather data is displayed on the extension page including the city name, actual-temperature, feelslike-temperature, weather description, clouds and an icon representing the weather condition. The icon (images of weather condition) is fetched from the API itself.


## Merits of SkyScan:

- <u>**Responsive Design**</u>: The web page is designed to be responsive and adaptable to different screen sizes and devices.
- <u>**Smooth Animations:**</u>: Animations and transitions are added for a smoother user experience such as color transitions on hover, background images animation, etc.
- <u>**Background Image:**</u>: A dynamic background image is used to enhance the visual appeal of the extension.


## De-merits of ScyScan:

- The extension cannot fetch the weather data of current location of the user. I've tried but couldn't succeed in adding this feature. 
- As I'm a beginner in developing a chrome extension and first-time user of API, SkyScan is a minimal kind of weather extension and it only displays the temperatures, clouds info, etc. I could not add features like humidity, wind speed, sunrise/sunset timings, hourly data of the weather,etc.
- The SkyScan extension displays the temperature only in Celcius. I tried to add fahrenheit and kelvin units (actually can do it by writing the math-code for conversion of units), but it felt complicated for me while developing the extension.
- SkyScan does not save a default location given by the user (user's favorite city as default) as I'm not familiar and do not have an idea how this feature works.


## Conclusion:

"SkyScan" is a bminimal-handy weather extention that is developed for people like Kalashnikov, which will keep him well informed about the weather at his next rendezvous location so that he could be well prepared and could  be dressed accordingly to not get reprimanded by his superiors again 😃.

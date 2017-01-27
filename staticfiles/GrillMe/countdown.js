var Timer = function(duration,id)
{
     // Property: Frequency of elapse event of the timer in millisecond
    this.Interval = 1000;

    // Property: Whether the timer is enable or not
    this.Enable = new Boolean(false);

    // Div class
    this.id = id;

        // Member variable: Hold interval id of the timer
    var timerId = 0;

    // Member variable: Hold instance of this class
    var thisObject;

    var timer = duration


    // Event: Timer tick
    this.Tick = function updateClock() {

                        var clock = document.getElementById(this.id);
                        var hoursSpan = clock.querySelector('.hours');
                        var minutesSpan = clock.querySelector('.minutes');
                        var secondsSpan = clock.querySelector('.seconds');

                        var minutes = parseInt((timer / 60) % 60, 10);
                        var seconds = parseInt(timer % 60, 10);
                        var hours = parseInt((timer / (60 * 60)) % 60,10);

                        minutes = minutes < 10 ? "0" + minutes : minutes;
                        seconds = seconds < 10 ? "0" + seconds : seconds;
                        hours = hours < 10 ? "0" + hours : hours;

                        hoursSpan.innerHTML = ('0' + hours).slice(-2);
                        minutesSpan.innerHTML = ('0' + minutes).slice(-2);
                        secondsSpan.innerHTML = ('0' + seconds).slice(-2);

                        if (--timer < 0) {
                            timer = 0;
                        }
                };

        // Function: Start the timer
    this.Start = function()
    {
        this.Enable = new Boolean(true);

        thisObject = this;
        if (thisObject.Enable)
        {
            thisObject.timerId = setInterval(
            function()
            {
                thisObject.Tick();
            }, thisObject.Interval);
        }
    };

    // Function: Stops the timer
    this.Stop = function()
    {
        thisObject.Enable = new Boolean(false);
        clearInterval(thisObject.timerId);
    };

    this.Reset = function()
    {
        timer = duration
        this.Tick();
        this.Stop();
    }



};

var myTimer = new Timer(100,'clockdiv');
'''
Created on 7/12/2015

@author: sdo

Inspired by the Iron Python progress bar by minrk (Github)
'''
import sys, time

class ProgressBar:
    """You should instciate the progreee bar right before you use it,
    as the timer starts when the class in intialised."""
    def __init__(self, max_value, iterword="samples", bar_length=50):
        self.max_value = max_value      # The max number of units
        self.bar_length = bar_length    # Number of chars
        self.prog_bar = '[]'
        self.fill_char = '#'
        self.__update_amount(0)
        self.animate = self.animate_python
        self.lasttime = time.time()
        self.current_iter = 0
        self.iterword = iterword
        
    def update_paced(self):
        """Called once per loop, as an alternative to animate_python"""
        self.animate_python(self.current_iter)
        self.current_iter += 1
    
    def update_thread(self):
        """Update the timer, without incrimenting the counter"""
        self.animate_python(self.current_iter)
        
    def reset(self):
        self.current_iter = 0
        self.lasttime = time.time()

    def animate_python(self, current_iter):
        self.update_iteration(current_iter)
        sys.stdout.write('\r' + self.prog_bar)
        sys.stdout.flush()

    def update_iteration(self, elapsed_iter):
        try:
            # Catch the case where update is called with 0 as the max value
            self.__update_amount((elapsed_iter / float(self.max_value)) * 100.0)
        except:
            pass
        seconds = time.time() - self.lasttime
        minutes = int(seconds / 60)
        hours = int(minutes / 60)
        seconds = seconds % 60
        minutes = minutes % 60
        self.prog_bar += '  %d %s of %d complete\t %.2d:%.2d:%.2d' % (elapsed_iter, self.iterword, self.max_value, hours, minutes, seconds) # try %2.d for spacing and no 0 padding

    def __update_amount(self, new_amount):
        percent_done = int(round((new_amount / 100.0) * 100.0))
        all_full = self.bar_length - 2 # The two square brackets []
        num_hashes = int(round((percent_done / 100.0) * all_full))
        self.prog_bar = '[' + self.fill_char * num_hashes + ' ' * (all_full - num_hashes) + ']'
        pct_place = (len(self.prog_bar) / 2) - len(str(percent_done))
        pct_string = '%d%%' % percent_done
        self.prog_bar = self.prog_bar[0:pct_place] + \
            (pct_string + self.prog_bar[pct_place + len(pct_string):])

    def __str__(self):
        return str(self.prog_bar)

class Display_Time(object):
    lasttime = time.time()
    uptime = 0
    totalreloads = 0
    
    def Reload(self):
        """Return the number of seconds since the instasiation (or reload)"""
        seconds = time.time() - self.lasttime
        self.lasttime = seconds
        self.Update(seconds)
        
        self.totalreloads += 1
        self.uptime += seconds
        return seconds
    
    def Update(self, seconds):
        """Update the number of hours, minutes, seconds."""
        minutes = int(seconds / 60)
        self.hours = int(minutes / 60)
        self.seconds = seconds % 60
        self.minutes = minutes % 60
    
    def Load_New_Time(self, timedelta):
        self.Update(timedelta.total_seconds())
       
    def __repr__(self):
        return "%.2d:%.2d:%.2d" % (self.hours, self.minutes, self.seconds)

class TestProgressBar():
    def __init__(self, itters=800):
        print "Testing the progress bar with a count of 800 units (8 seconds)"
    
        p = ProgressBar(itters)
        for i in range(itters + 1):
            p.animate(i)
            time.sleep(0.01)
        print
        
    def __repr__(self):
        return "Progress Bar"
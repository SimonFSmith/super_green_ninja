class Publisher:

    def __init__(self, events):
        self.events = { event : dict() for event in events }
    

    # get subscribers for this specific event
    def get_subscribers(self, event):
        return self.events[event]
    

    # add event listener
    def register(self, event, subscriber, handler):
        self.get_subscribers(event)[subscriber] = handler
     

    # remove event listener
    def unregister(self, event, subscriber):
        del self.get_subscribers(event)[subscriber]
      
      
    # throw event
    def dispatch_event(self, event):
        for sub, handler in self.get_subscribers(event).items():
            handler()

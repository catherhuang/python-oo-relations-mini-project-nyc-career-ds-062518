class Invite:
    _all = []
    def __init__(self, dinner_party, guest, rsvp_status=False):
        self._name= guest
        self._dinner_party=dinner_party
        self._rsvp_status=rsvp_status
        Invite.all().append(self)

    @property
    def guest(self):
        return self._name
    @property
    def dinner_party(self):
        return self._dinner_party
    @classmethod
    def all(cls):
        return Invite._all
    @property
    def rsvp_status(self):
        return self._rsvp_status
    def rsvp_stats(self, status):
        self._rsvp_status = status
    def accepted(self):
        if self.rsvp_status != False: 
            return 0

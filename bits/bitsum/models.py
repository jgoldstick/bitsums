from django.db import models
"""
BitSum contains two integers, the number of binary ones in the product of
the integers (A and B), and the time at which it was calculated.  The
used value is the ordinal of the runs
"""


class BitSum(models.Model):
    time = models.DateTimeField(db_index=True)
    bitsum = models.PositiveIntegerField()
    A = models.PositiveIntegerField()
    B = models.PositiveIntegerField()
    used = models.PositiveIntegerField(db_index=True)

    def __unicode__(self):
        return "%d * %d = %s used: %d" % (self.A, self.B, self.bitsum, self.used)

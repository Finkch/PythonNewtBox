# Static constants

from decimal import Decimal

# Gravitational constant
G: Decimal = Decimal('6.6743015e-11')

# Astronomical unit
AU: Decimal = Decimal('1.496e11')

# Time
SECOND: Decimal = Decimal(1)
MINUTE: Decimal = SECOND * 60
HOUR:   Decimal = MINUTE * 60
DAY:    Decimal = HOUR * 24
YEAR:   Decimal = DAY * Decimal('365.24')

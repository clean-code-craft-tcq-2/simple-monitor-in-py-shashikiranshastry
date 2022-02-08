class Range:
  def __init__(self, parameter, min_limit, max_limit):
    self.parameter = parameter
    self.min_limit = min_limit
    self.max_limit = max_limit

temperature_range = Range("Temperature",0, 45)
soc_range = Range("State of Charge",20, 80)
charge_rate_range = Range("Charge Rate",0, 0.8)

class CheckLimit:
  def __init__(self, value, range):
    self.value = value
    self.range = range
  
  def check_limit(self):
    withinLimit = False
    if self.value > self.range.max_limit:
      print(self.range.parameter + ' is exceeding the maximum limit!')
    elif self.value < self.range.min_limit:
      print(self.range.parameter + ' is below minimum limit!')
    else:
      withinLimit = True
      
    return withinLimit
  
def battery_is_ok(temperature, soc, charge_rate):
  temperature_check = CheckLimit(temperature, Range.temperature_range)
  soc_check = CheckLimit(soc, Range.soc_range)
  charge_rate_check = CheckLimit(charge_rate, Range.charge_rate_range)
  
  return temperature_check.check_limit() and soc_check.check_limit() and charge_rate_check.check_limit()

def TestBattery():
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
  assert(battery_is_ok(20, 60, 0.9) is False)
  assert(battery_is_ok(20, 60, 0.1) is True)
  assert(battery_is_ok(1000, 900, 10) is False)
  
if __name__ == '__main__':
    TestBattery()

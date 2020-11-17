import swas
from swas import info

def test_module():
  assert info.yt()
  j = info.userinfo()
  assert j.name
  assert j.id
  assert j.discriminator
  assert swas.__version__
  assert swas.__license__

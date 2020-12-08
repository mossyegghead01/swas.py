import swas

def test_module():
  assert swas.info.yt()
  j = swas.info.userinfo()
  assert j.name
  assert j.id
  assert j.discriminator
  assert swas.__version__
  assert swas.__license__

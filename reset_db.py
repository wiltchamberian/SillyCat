from models import *

with app.app_context():
  db.drop_all()
  db.create_all()
  new_user = User(name='wiltchamberian')
  db.session.add(new_user)
  file = File(guid='a10c7246-791a-4e78-9741-86902a7b960f',
              user = 'wiltchamberian',
              title = 'Allen',
              publish_time = '27.July.2024',
              content = "This is eistein's famous formula: \\(E=mc^2\\) \n it is concise")
  db.session.add(file)
  file2 = File(guid='b84e67f3-2b95-46a7-81f5-9e072d3e0b7e',
               user = 'wiltchamberian',
               title = 'Alice')
  db.session.add(file2)
  db.session.commit()

if __name__ == '__main__':
  print("hello world!")
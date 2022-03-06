from app.main.views import comment
from app.models import Commnet,User
from app import db
from werkzeug import secure_filename,FileStorage



def setUp(self):
        self.user_kimutaiamos = User(username = 'kimutaiamos',password = 'savanna', email = 'amos.kimutai@student.moringaschoo.com')
        self.new_comment = comment(pitch_title='movie',pitch="the heritage was from a history",pitch_comment='This pitch is the best thing since sliced bread',user = self.user_Rotich )

def tearDown(self):
        comment.query.delete()
        User.query.delete()

def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.pitch_title,'Comment for pitches')
        self.assertEquals(self.new_comment.pitch,"the heritage was from a history")
        self.assertEquals(self.new_comment.pitch_comment,'This pitch is the best thing since sliced bread')
        self.assertEquals(self.new_Comment.user,self.user_Rotich)

def test_get_Comment_by_id(self):

        self.new_comment.save_comment()
        got_comments = comment.get_comments(12345)
        self.assertTrue(len(got_comments) == 1)
import unittest
from BucketList import BucketList


class TestBucket(unittest.TestCase):
    """
       Class performing unit testing for class BucketList
    """

    # Defining setUp() method that runs prior to each test.
    def setUp(self):
        self.bucket = BucketList()

    # defining method to test for adding a bucket list
    def test_for_adding_bucketlist(self):
        self.bucket.bucket_list = {}
        expect = {'success': 'Bucket list added successfully'}
        res = self.bucket.add_bucket_list('Bucketlist 1', 'Fashion', 'Nairobi', '12-12-12', 'this is a bucket', 'ian')

        self.assertEqual(res, expect)

    # defining method to test for adding similar bucket lists
    def test_for_adding_similar_bucket(self):
        expect = {'error': 'Title already taken'}
        self.bucket.add_bucket_list('Bucketlist 1', 'Fashion', 'Nairobi', '12-12-12', 'this is a bucket', 'ian')
        res = self.bucket.add_bucket_list('Bucketlist 1', 'Fashion', 'Nairobi', '12-12-12', 'this is a bucket', 'ian')

        self.assertEqual(res, expect)

    # defining method to test for updating an existing bucket list
    def test_update_bucket_list(self):
        expect = {'success': 'Bucket list updated successfully'}
        res = self.bucket.update_bucket_list('Updated', 'Fashion', 'Location', '12-12-12', 'desc', 'ian')

        self.assertEqual(expect, res)

    # defining method to test for adding a bucket list check list
    def test_add_bucket_list_check_list(self):
        self.bucket.bucket_list = {}
        self.bucket.add_bucket_list('Bucketlist 1', 'Fashion', 'Nairobi', '12-12-12', 'this is a bucket', 'ian')
        expect = {'success': 'Step added successfully'}
        res = self.bucket.add_step('Bucketlist 1', 'visit kicc')

        self.assertEqual(expect, res)

    # defining method to test for adding a bucket list checklist to a non existing bucket list
    def test_add_step_to_a_non_existing_bucket(self):
        expect = {'error': 'Step could not be added'}
        res = self.bucket.add_step('Bucketlist 2', 'visit kicc')

        self.assertEqual(expect, res)

    # defining method to test for getting all bucket lists
    def test_get_bucket_list(self):
        self.bucket.bucket_list = {}
        expect = {'Bucketlist 7': {'category': 'Fashion',
                                   'check_list': None,
                                   'date': '12-12-12',
                                   'description': 'this is a bucket',
                                   'location': 'Nairobi',
                                   'status': 'Active',
                                   'title': 'Bucketlist 7',
                                   'user_id': 'ian'}}
        self.bucket.add_bucket_list('Bucketlist 7', 'Fashion', 'Nairobi', '12-12-12', 'this is a bucket', 'ian')
        res = self.bucket.get_bucket_list()
        self.assertEqual(expect, res)

    # defining method to test for adding all bucket list checklists
    def test_to_get_bucket_list_checklist(self):
        self.bucket.bucket_list = {}
        self.bucket.add_bucket_list('Bucketlist 1', 'Fashion', 'Nairobi', '12-12-12', 'this is a bucket', 'ian')
        res = self.bucket.add_step('Bucketlist 1', "Step")
        expect = {'success': 'Step added successfully'}

        self.assertEqual(expect, res)

    # defining method to test for deleting a bucket list
    def test_to_delete_bucket_list(self):
        self.bucket.bucket_list = {}
        self.bucket.add_bucket_list('Bucketlist 1', 'Fashion', 'Nairobi', '12-12-12', 'this is a bucket', 'ian')
        res = self.bucket.del_bucket_list("Bucketlist 1")
        expect = {'success': 'Bucketlist deleted successfully'}

        self.assertEqual(expect, res)

    # defining method to test for deleting a non existing bucket list
    def test_for_delete_of_non_existsing_bucket_list(self):
        self.bucket.bucket_list = {}
        res = self.bucket.del_bucket_list("Bucketlist 1")
        expect = {'error': 'Bucketlist could not be deleted'}

        self.assertEqual(expect, res)

    # defining method to test for adding a step to bucket list
    def test_add_step_to_bucket_list(self):
        self.bucket.bucket_list = {}
        self.bucket.add_bucket_list('Bucketlist 1', 'Fashion', 'Nairobi', '12-12-12', 'this is a bucket', 'ian')
        res = self.bucket.add_step("Bucketlist 1", "title")
        expect = {'success': 'Step added successfully'}

        self.assertEqual(res, expect)

    # defining method to test for adding a step to non existing bucket list
    def test_add_step_to_non_existence_bucket_list(self):
        self.bucket.bucket_list = {}
        self.bucket.add_bucket_list('Bucketlist 1', 'Fashion', 'Nairobi', '12-12-12', 'this is a bucket', 'ian')
        res = self.bucket.add_step("Bucketlist 5", "title")
        expect = {'error': 'Step could not be added'}

        self.assertEqual(res, expect)

if __name__ == "__main__":
    unittest.main()

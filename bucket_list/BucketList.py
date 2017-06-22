class BucketList(object):

    # Defining static variables
    bucket_list = dict()
    goal_status = ['Active', 'Completed']
    category_list = [
        'Nature', 'Health', 'Fashion', 'Food', 'Travel', 'Business', 'Education', 'Family',
    ]

    # Initializing class instance variables
    def __init__(self):
        self.title = None
        self.description = None
        self.category = None
        self.location = None
        self.date = None
        self.check_list = dict()
        self.status = 'Active'
        self.user_id = None

    # defining method to add bucket list
    def add_bucket_list(self, title, category, location, date, desc, user_id):

        msg = {
            'error': "Fill all Fields"
        }

        if title is not None and title != '' and category is not None and category != '' and desc is not None:
            if desc != '' and location is not None and location != '' and date != '' and date is not None:
                self.title = title
                self.category = category
                self.location = location
                self.date = date
                self.description = desc
                self.user_id = user_id

                msg = self.save_data()
                return msg
        return msg

    # defining method to update bucket list
    def update_bucket_list(self, title, category, location, date, desc, user_id):

        msg = {
            'error': "Fill all Fields"
        }

        if title is not None and title != '' and category is not None and category != '' and desc is not None:
            if desc != '' and location is not None and location != '' and date != '' and date is not None:
                self.title = title
                self.category = category
                self.location = location
                self.date = date
                self.description = desc
                self.user_id = user_id

                msg = self.update_bucket_data()
                return msg
        return msg

    # defining method to update bucket list
    def update_bucket_list_status(self, bucket_list, status):

        msg = {
            'error': "Sorry, status could not be updated"
        }
        if bucket_list in self.bucket_list.keys():
            if status in self.goal_status:
                # confirm all step status are correct

                if self.bucket_list[bucket_list]['check_list']:
                    msg = {
                        'success': "Status updated successfully"
                    }

                    for item in self.bucket_list[bucket_list]['check_list']:
                        if self.bucket_list[bucket_list]['check_list'][item]['status'] == 'Active':
                            msg = {
                                'error': 'All steps are not completed'
                            }

                if 'success' in msg.keys():
                    self.bucket_list[bucket_list]['status'] = status

        return msg

    # defining helper method to save bucket list data
    def save_data(self):
        msg = {
            'error': "Category provided does not exist"
        }
        if self.category in self.category_list:
            if self.title not in self.bucket_list.keys():
                self.bucket_list[self.title] = {
                    'title': self.title,
                    'description': self.description,
                    'category': self.category,
                    'check_list': None,
                    'status': 'Active',
                    'date': self.date,
                    'location': self.location,
                    'user_id': self.user_id,
                }
                msg = {
                    'success': "Bucket list added successfully"
                }

            else:
                msg = {
                    'error': "Title already taken"
                }
        return msg

    # defining method to update bucket list data
    def update_bucket_data(self):
        msg = {
            'error': "Could not update bucketlist"
        }
        if self.category in self.category_list:
            # if self.title in self.bucket_list.keys():
                self.bucket_list[self.title] = {
                    'title': self.title,
                    'description': self.description,
                    'category': self.category,
                    'check_list': None,
                    'status': 'Active',
                    'date': self.date,
                    'location': self.location,
                    'user_id': self.user_id,
                }
                msg = {
                    'success': "Bucket list updated successfully"
                }
        return msg

    # defining method to add item checklists to a bucket list
    def add_step(self, bucket_list, title):
        msg = {
            'error': 'Step could not be added'
        }
        if title not in self.check_list.keys():

            if bucket_list in self.bucket_list.keys():
                self.check_list[title] = {
                    'title': title,
                    'status': self.status,
                    'bucket_list': bucket_list,
                }
                self.bucket_list[bucket_list]['check_list'] = self.check_list

                msg = {
                    'success': 'Step added successfully'
                }
        return msg

    # defining method to update bucket list checklist status
    def update_step_status(self, bucket_list, title, status):

        msg = {
            'error': "Sorry, step could not be updated"
        }

        if bucket_list in self.bucket_list.keys():
            if title in self.bucket_list[bucket_list]['check_list'].keys():
                if status in self.goal_status:
                    self.bucket_list[bucket_list]['check_list'][title]['status'] = status
                    self.update_bucket_list_status(bucket_list, status)
                    msg = {
                        'success': "Step status updated successfully"
                    }
        return msg

    # defining method to delete bucket list checklist
    def del_step(self, bucket_list, title):

        msg = {
            'error': "Sorry, step could not be deleted"
        }

        if bucket_list in self.bucket_list.keys():

            if title in self.bucket_list[bucket_list]['check_list'].keys():
                self.bucket_list[bucket_list]['check_list'].pop(title)
                msg = {
                    'success': "Step deleted successfully"
                }
        return msg

    # defining method to get all bucket lists
    def get_bucket_list(self):
        return self.bucket_list

    # defining method to get all bucket list checklists
    def get_checklist(self):
        return self.check_list

    # defining method to delete a specific bucket list
    def del_bucket_list(self, title):
        msg = {
            'error': 'Bucketlist could not be deleted'
        }
        if title in self.bucket_list.keys():

            self.bucket_list.pop(title)
            msg = {
                'success': 'Bucketlist deleted successfully',
            }

        return msg


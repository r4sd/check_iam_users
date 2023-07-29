import boto3
import os

def main():
    # プロファイル名は、任意で指定してね
    session = boto3.Session(profile_name='xxxxx')

    iam = session.client('iam')

    if not os.path.exists('user.lists'):
        print("user.lists is not found.")
        return

    with open('user.lists', 'r') as f:
        expected_users = [line.strip() for line in f]

    aws_users = iam.list_users()
    aws_user_names = [user['UserName'] for user in aws_users['Users']]
    extra_users = set(aws_user_names) - set(expected_users)

    with open('delete_user.lists', 'w') as f:
        for user in extra_users:
            f.write(user + '\n')

if __name__ == "__main__":
    main()

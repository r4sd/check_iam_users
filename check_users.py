import boto3

def main():
    # プロファイル名は、任意で指定してね
    session = boto3.Session(profile_name='xxxxx')

    # Initialize the IAM client
    iam = session.client('iam')

    # Read the expected users from a file
    with open('user.lists', 'r') as f:
        expected_users = [line.strip() for line in f]

    # Get the list of users from AWS IAM
    aws_users = iam.list_users()
    aws_user_names = [user['UserName'] for user in aws_users['Users']]

    # Find users that are in AWS IAM but not in the expected users list
    extra_users = set(aws_user_names) - set(expected_users)

    # Write the extra users to a file
    with open('delete_user.lists', 'w') as f:
        for user in extra_users:
            f.write(user + '\n')

if __name__ == "__main__":
    main()

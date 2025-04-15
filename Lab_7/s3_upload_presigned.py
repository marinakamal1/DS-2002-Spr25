import boto3

# Initialize the S3 client
s3 = boto3.client('s3', region_name='us-east-1')

# File and bucket details
bucket_name = 'my-unique-bucket-name-marinakamal123'
file_path = '/Users/marinakamal/Documents/Synaptic Neurons.jpg'  # Path to 
your file
object_name = 'Synaptic Neurons.jpg'  # Desired name of the file in the S3 
bucket

# Upload the file (without public-read ACL)
try:
    s3.upload_file(file_path, bucket_name, object_name)
    print("✅ File uploaded successfully (private by default).")
    
    # Generate a presigned URL valid for 1 hour (3600 seconds)
    url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': object_name},
        ExpiresIn=3600
    )
    print(f"🔗 Presigned URL (valid 1 hour):\n{url}")
    
except Exception as e:
    print(f"❌ An error occurred: {e}")

import requests

def get_ip_location(ip_address):
    try:
        response = requests.get(f'https://ipapi.co/{ip_address}/json/')
        if response.status_code == 200:
            data = response.json()
            return {
                'ip': data.get('ip'),
                'country': data.get('country_name'),
                'region': data.get('region'),
                'city': data.get('city'),
                'latitude': data.get('latitude'),
                'longitude': data.get('longitude'),
                'postal_code': data.get('postal'),
                'time_zone': data.get('timezone'),
                'org': data.get('org')
            }
        else:
            print(f"Error: Unable to fetch data. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error getting location: {e}")
        return None

def analyze_ip():
    ip = input("Enter an IP address: ")
    location = get_ip_location(ip)
    if location:
        print(f"\nLocation information for IP: {location['ip']}")
        print(f"Country: {location['country'] or 'Unknown'}")
        print(f"Region: {location['region'] or 'Unknown'}")
        print(f"City: {location['city'] or 'Unknown'}")
        print(f"Postal Code: {location['postal_code'] or 'Unknown'}")
        print(f"Latitude: {location['latitude']}")
        print(f"Longitude: {location['longitude']}")
        print(f"Time Zone: {location['time_zone'] or 'Unknown'}")
        print(f"Organization: {location['org'] or 'Unknown'}")
    else:
        print("Could not determine location for the given IP address")

if __name__ == "__main__":
    analyze_ip()

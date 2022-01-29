from azure.iot.device.provisioning.provisioning_device_client import ProvisioningDeviceClient
#from azure.iot.device.provisioning.provisioning_device_client import IoTHubDeviceClient
from azure.iot.device.iothub.sync_clients import IoTHubDeviceClient

def provision_device(provisioning_host, id_scope, registration_id, symmetric_key, model_id):
    provisioning_device_client = ProvisioningDeviceClient.create_from_symmetric_key(
        provisioning_host=provisioning_host,
        registration_id=registration_id,
        id_scope=id_scope,
        symmetric_key=symmetric_key,
    )

    provisioning_device_client.provisioning_payload = {"modelId": model_id}
    return provisioning_device_client.register()

provisioning_host = "global.azure-devices-provisioning.net"
id_scope = "0ne0007F49A" 
registration_id = "40c62aa8-3fba-47a2-9e62-1fee378cfc7c"
symmetric_key = "+EQYUjhFMxtijdU8KT0h5uTXEO8dLQvxWoPnJgrC3gI="
registration_result = provision_device(provisioning_host, id_scope, registration_id, symmetric_key, None)

print(registration_result.status)
if registration_result.status == "assigned":
    print("Device was assigned")
    print(registration_result.registration_state.assigned_hub)
    print(registration_result.registration_state.device_id)
    device_client = IoTHubDeviceClient.create_from_symmetric_key(
    symmetric_key=symmetric_key,
    hostname=registration_result.registration_state.assigned_hub,
    device_id=registration_result.registration_state.device_id,
    product_info=None,)
    device_client.connect()
    air_temperature = "10"
    humidity = "20"
    co2 = "30"
    dust_1 = "40"
    dust_2 = "50"
    dust_10 = "60"
    co_m = "70"
    high_ozon = "80"
    low_ozon = "90"
    device_client.send_message("{ \
\"AirTemp\": " + air_temperature + ", \
\"Humidity\": " + humidity + ", \
\"CO2\": " + co2 + ", \
\"Dust1\": " + dust_1 + ", \
\"Dust2\": " + dust_2 + ", \
\"Dust10\": " + dust_10 + ", \
\"CO\": " + co_m + ", \
\"HighOzone\": " + high_ozon + ", \
\"LowOzone\": " + low_ozon + ", \
\"accelerometerZ\": " + "1" + "}")





else:
    raise RuntimeError(
                "Could not provision device. Aborting Plug and Play device connection."
            )




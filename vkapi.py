import vk
import json
import requests
import tempfile

session = vk.Session()
api = vk.API(session, v=5.0)


def send_message(user_id, token, message, attachment=""):
    if(attachment!=""):
        data = api.photos.getMessagesUploadServer(access_token=token, user_id=str(user_id))
        upload_url = data["upload_url"]
        response = requests.get(attachment)
        if response.status_code == 200:
            fp = tempfile.NamedTemporaryFile(suffix='.png')
            fp.write(response.content)
            fp.seek(0)
            files = {'photo': fp}
            r = requests.post(upload_url, files=files)
            fp.close()
            result = json.loads(r.text)
            uploadResult = api.photos.saveMessagesPhoto(access_token = token, server=result["server"], photo=result["photo"], hash=result["hash"])
            api.messages.send(access_token = token, user_id=user_id, message=message, attachment = 'photo' + str(uploadResult[0]['owner_id']) + '_' + str(uploadResult[0]['id']))
    else:
        api.messages.send(access_token=token, user_id=str(user_id), message=message, attachment=attachment)
    return


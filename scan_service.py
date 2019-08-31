from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask import request
app = Flask(__name__)
api = Api(app)

'''
atpBackupScanArgs:
{
  "scanType"    : "last/all/restore",
  "intentionId" : "00000000-0000-0000-0000-000000000000",
  "vaultId"     : "00000000-0000-0000-0000-000000000000",
  "archiveId"   : "00000000-0000-0000-0000-000000000000",
  "credId?"     : "External credential ID (if archive is password protected)",
  "archiveUri"  : "Archive URI",
  "tenantId"    : int64,
  "scanAV"      : true,
  "scanVA"      : true
}
'''

@app.route('/scan_service/api/1/scan', methods=['POST'])
def create_scan_session():
    if not request.json:
        print('request.json')
        abort(400)
    if not 'intentionId' in request.json:
        print('intentionId')
        abort(400)
    if not 'firstSlice' in request.json:
        print('firstSlice')
        abort(400)
    if not 'lastSlice' in request.json:
        print('lastSlice')
        abort(400)
    print('intentionId', request.json['intentionId'])
    print('firstSlice', request.json['firstSlice'])
    print('lastSlice', request.json['lastSlice'])
    rspns = {
        'scanId': '063ec4ac-7cf9-466c-9f23-5022909b66e0',
        'scanToSlice': {
            'sliceId': '758116ce-325f-41de-99f2-563d18d31087',
            'created': 645342
        }
    }
    return jsonify(rspns), 201

if __name__ == '__main__':
    app.run(debug=True)
# Alex's snippet
@pytest.fixture
def deposit_file(deposit, db):
    """Deposit files."""
    BLR_USER = 	1  # Create the user
    with app.test_request_context():
        datastore = app.extensions['security'].datastore
        login_user(datastore.get_user(BLR_USER))
        id_ = uuid4()
        zenodo_deposit_minter(id_, deposit_metadata)  # metadata from JSONL file
        deposit = Deposit.create(deposit_metadata, id_=id_)
        db_.session.commit()
    current_search.flush_and_refresh(index='deposits')
    return deposit

    html_file = open('out/12345.html')
    deposit.files['treatment.html'] = html_file

    xml_file = open('data/12345.xml')
    deposit.files['.hidden/application/vnd.plazi+xml'] = xml_file
    deposit.publish()
    db.session.commit()
    return deposit.files


### Local Token
token = 'yV66Li6vIUKWD9O50NgT5rOIDTK4tzk2URDW3vm0B9WMplXCA9iALeKX2JOu'

### Zenodo Side
metadata = {
        'title': 'My second upload',
        'upload_type': 'publication',
        'publication_type': 'book',
        'description': 'This is my first upload',
        'access_right': 'open',
        'license': 'cc-by',
        'creators': [{'name': 'Doe, John', 'affiliation': 'Zenodo'}]
    }

upload_test(token)
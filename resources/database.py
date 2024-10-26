from pydo import Client
from resources.project import Project
class PGDB:
    def __init__(self,token,dbname,projectname):
        self.token=token
        self.dbname=dbname
        self.client = Client(token=token) 
        self.projectname=projectname
        self.project=Project(self.token,self.projectname)
        self.exists,self.dbproperties=self._check_if_exists()
    def _getalldbclusters(self):
        db_clusters=self.client.databases.list_clusters()
        return db_clusters
    def _check_if_exists(self):
        project_id=self.project.project_id
        exists=False
        d=False
        if project_id:
            for d in self._getalldbclusters()['databases']:
                if d['project_id']==project_id and d['name']==self.dbname:
                    exists=True
        return exists,d
    def create_db_cluster(self):
        body = {
            "engine": "pg",  # A slug representing the database engine used for the
            #cluster. The possible values are: "pg" for PostgreSQL, "mysql" for MySQL, "redis"
            #for Redis, "mongodb" for MongoDB, "kafka" for Kafka, and "opensearch" for
            #OpenSearch. Required. Known values are: "pg", "mysql", "redis", "mongodb",
            #"kafka", and "opensearch".
            "name": f"{self.dbname}",  # A unique, human-readable name referring to a database
            #cluster. Required.
            "num_nodes": 1,  # The number of nodes in the database cluster. Required.
            "region": "fra1",  # The slug identifier for the region where the database
            #cluster is located. Required.
            "size": "db-s-1vcpu-1gb",  # The slug identifier representing the size of the nodes in
            #the database cluster. Required.
            #"backup_restore": {
            #    "database_name": "str",  # The name of an existing database cluster
            #    from which the backup will be restored. Required.
            #    "backup_created_at": "2020-02-20 00:00:00"  # Optional. The timestamp
            #    of an existing database cluster backup in ISO8601 combined date and time
            #    format. The most recent backup will be used if excluded.
            #},
            "connection": {
                "database": "defaultdb",  # Optional. The name of the default database.
                #"host": "str",  # Optional. The FQDN pointing to the database
                #cluster's current primary node.
                "password": "postgis",  # Optional. The randomly generated password for
                #the default user.
                #"port": 0,  # Optional. The port on which the database cluster is
                #listening.
                #"ssl": bool,  # Optional. A boolean value indicating if the
                #connection should be made over SSL.
                #"uri": "str",  # Optional. A connection string in the format accepted
                #by the ``psql`` command. This is provided as a convenience and should be able
                #to be constructed by the other attributes.
                "user": "postgres"  # Optional. The default user for the database.
            },
            #"created_at": "2020-02-20 00:00:00",  # Optional. A time value given in
            #ISO8601 combined date and time format that represents when the database cluster
            #was created.
            "db_names": [
                "postgis_test"  # Optional. An array of strings containing the names of
                #databases created in the database cluster.
            ],
            #"id": "str",  # Optional. A unique ID that can be used to identify and
            #reference a database cluster.
            #"maintenance_window": {
            #    "day": "str",  # The day of the week on which to apply maintenance
            #    updates. Required.
            #    "hour": "str",  # The hour in UTC at which maintenance updates will
            #    be applied in 24 hour format. Required.
            #    "description": [
            #        "str"  # Optional. A list of strings, each containing
            #        information about a pending maintenance update.
            #    ],
            #    "pending": bool  # Optional. A boolean value indicating whether any
            #    maintenance is scheduled to be performed in the next window.
            #},
            #"metrics_endpoints": [
            #    {
            #        "host": "str",  # Optional. A FQDN pointing to the database
            #        cluster's node(s).
            #        "port": 0  # Optional. The port on which a service is
            #        listening.
            #    }
            #],
            #"private_connection": {
            #    "database": "str",  # Optional. The name of the default database.
            #    "host": "str",  # Optional. The FQDN pointing to the database
            #    cluster's current primary node.
            #    "password": "str",  # Optional. The randomly generated password for
            #    the default user.
            #    "port": 0,  # Optional. The port on which the database cluster is
            #    listening.
            #    "ssl": bool,  # Optional. A boolean value indicating if the
            #    connection should be made over SSL.
            #    "uri": "str",  # Optional. A connection string in the format accepted
            #    by the ``psql`` command. This is provided as a convenience and should be able
            #    to be constructed by the other attributes.
            #    "user": "str"  # Optional. The default user for the database.
            #},
            #"private_network_uuid": "str",  # Optional. A string specifying the UUID of
            #the VPC to which the database cluster will be assigned. If excluded, the cluster
            #when creating a new database cluster, it will be assigned to your account's
            #default VPC for the region.
            "project_id": f"{self.project.project_id}",  # Optional. The ID of the project that the database
            #cluster is assigned to. If excluded when creating a new database cluster, it will
            #be assigned to your default project.
            #"rules": [
            #    {
            #        "type": "str",  # The type of resource that the firewall rule
            #        allows to access the database cluster. Required. Known values are:
            #        "droplet", "k8s", "ip_addr", "tag", and "app".
            #        "value": "str",  # The ID of the specific resource, the name
            #        of a tag applied to a group of resources, or the IP address that the
            #        firewall rule allows to access the database cluster. Required.
            #        "cluster_uuid": "str",  # Optional. A unique ID for the
            #        database cluster to which the rule is applied.
            #        "created_at": "2020-02-20 00:00:00",  # Optional. A time
            #        value given in ISO8601 combined date and time format that represents when
            #        the firewall rule was created.
            #        "uuid": "str"  # Optional. A unique ID for the firewall rule
            #        itself.
            #    }
            #],
            #"semantic_version": "str",  # Optional. A string representing the semantic
            #version of the database engine in use for the cluster.
            #"standby_connection": {
            #    "database": "str",  # Optional. The name of the default database.
            #    "host": "str",  # Optional. The FQDN pointing to the database
            #    cluster's current primary node.
            #    "password": "str",  # Optional. The randomly generated password for
            #    the default user.
            #    "port": 0,  # Optional. The port on which the database cluster is
            #    listening.
            #    "ssl": bool,  # Optional. A boolean value indicating if the
            #    connection should be made over SSL.
            #    "uri": "str",  # Optional. A connection string in the format accepted
            #    by the ``psql`` command. This is provided as a convenience and should be able
            #    to be constructed by the other attributes.
            #    "user": "str"  # Optional. The default user for the database.
            #},
            #"standby_private_connection": {
            #    "database": "str",  # Optional. The name of the default database.
            #    "host": "str",  # Optional. The FQDN pointing to the database
            #    cluster's current primary node.
            #    "password": "str",  # Optional. The randomly generated password for
            #    the default user.
            #    "port": 0,  # Optional. The port on which the database cluster is
            #    listening.
            #    "ssl": bool,  # Optional. A boolean value indicating if the
            #    connection should be made over SSL.
            #    "uri": "str",  # Optional. A connection string in the format accepted
            #    by the ``psql`` command. This is provided as a convenience and should be able
            #    to be constructed by the other attributes.
            #    "user": "str"  # Optional. The default user for the database.
            #},
            #"status": "str",  # Optional. A string representing the current status of the
            #database cluster. Known values are: "creating", "online", "resizing",
            #"migrating", and "forking".
            #"storage_size_mib": 0,  # Optional. Additional storage added to the cluster,
            #in MiB. If null, no additional storage is added to the cluster, beyond what is
            #provided as a base amount from the 'size' and any previously added additional
            #storage.
            #"tags": [
            #    "str"  # Optional. An array of tags that have been applied to the
            #    database cluster.
            #],
            #"ui_connection": {
            #    "host": "str",  # Optional. The FQDN pointing to the opensearch
            #    cluster's current primary node.
            #    "password": "str",  # Optional. The randomly generated password for
            #    the default user.
            #    "port": 0,  # Optional. The port on which the opensearch dashboard is
            #    listening.
            #    "ssl": bool,  # Optional. A boolean value indicating if the
            #    connection should be made over SSL.
            #    "uri": "str",  # Optional. This is provided as a convenience and
            #    should be able to be constructed by the other attributes.
            #    "user": "str"  # Optional. The default user for the opensearch
            #    dashboard.
            #},
            #"users": [
            #    {
            #        "name": "str",  # The name of a database user. Required.
            #        "access_cert": "str",  # Optional. Access certificate for TLS
            #        client authentication. (Kafka only).
            #        "access_key": "str",  # Optional. Access key for TLS client
            #        authentication. (Kafka only).
            #        "mysql_settings": {
            #            "auth_plugin": "str"  # A string specifying the
            #            authentication method to be used for connections to the MySQL user
            #            account. The valid values are ``mysql_native_password`` or
            #            ``caching_sha2_password``. If excluded when creating a new user, the
            #            default for the version of MySQL in use will be used. As of MySQL
            #            8.0, the default is ``caching_sha2_password``. Required. Known values
            #            are: "mysql_native_password" and "caching_sha2_password".
            #        },
            #        "password": "str",  # Optional. A randomly generated password
            #        for the database user.
            #        "role": "str",  # Optional. A string representing the
            #        database user's role. The value will be either "primary" or "normal".
            #        Known values are: "primary" and "normal".
            #        "settings": {
            #            "acl": [
            #                {
            #                    "permission": "str",  # Permission
            #                    set applied to the ACL. 'consume' allows for messages to be
            #                    consumed from the topic. 'produce' allows for messages to be
            #                    published to the topic. 'produceconsume' allows for both
            #                    'consume' and 'produce' permission. 'admin' allows for
            #                    'produceconsume' as well as any operations to administer the
            #                    topic (delete, update). Required. Known values are: "admin",
            #                    "consume", "produce", and "produceconsume".
            #                    "topic": "str",  # A regex for
            #                    matching the topic(s) that this ACL should apply to.
            #                    Required.
            #                    "id": "str"  # Optional. An
            #                    identifier for the ACL. Will be computed after the ACL is
            #                    created/updated.
            #                }
            #            ],
            #            "opensearch_acl": [
            #                {
            #                    "index": "str",  # Optional. A regex
            #                    for matching the indexes that this ACL should apply to.
            #                    "permission": "str"  # Optional.
            #                    Permission set applied to the ACL. 'read' allows user to read
            #                    from the index. 'write' allows for user to write to the
            #                    index. 'readwrite' allows for both 'read' and 'write'
            #                    permission. 'deny'(default) restricts user from performing
            #                    any operation over an index. 'admin' allows for 'readwrite'
            #                    as well as any operations to administer the index. Known
            #                    values are: "deny", "admin", "read", "readwrite", and
            #                    "write".
            #                }
            #            ],
            #            "pg_allow_replication": bool  # Optional. For
            #            Postgres clusters, set to ``true`` for a user with replication
            #            rights. This option is not currently supported for other database
            #            engines.
            #        }
            #    }
            #],
            "version": "16"  # Optional. A string representing the version of the
            #database engine in use for the cluster.
            #"version_end_of_availability": "str",  # Optional. A timestamp referring to
            #the date when the particular version will no longer be available for creating new
            #clusters. If null, the version does not have an end of availability timeline.
            #"version_end_of_life": "str"  # Optional. A timestamp referring to the date
            #when the particular version will no longer be supported. If null, the version
            #does not have an end of life timeline.
        }
        resp=self.client.databases.create_cluster(body)
        self.exists,self.dbproperties=self._check_if_exists()
        return resp
    def delete_db_cluster(self):
        if self.exists:
            response=self.client.databases.destroy_cluster(self.dbproperties['id'])
            return response
        else:
            print("CANNOT DELETE DATABASE CLUSTER THAT DOES NOT EXIST")
            return False
            

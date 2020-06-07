# REST API:
A RESTful API is an application program interface (API) that uses HTTP requests to GET, PUT, POST and DELETE data.

An API for a website is code that allows two software programs to communicate with each other. The API spells out the proper way for a developer to write a program requesting services from an operating system or other application.

## RESTful API Design and Architecture Constraints:
RESTful API design was defined by Dr. Roy Fielding in his 2000 doctorate dissertation. In order to be a true RESTful API, a web service must adhere to the following six REST architectural constraints:

__1. Use of a uniform interface (UI).__ Resources should be uniquely identifiable through a single URL, and only by using the underlying methods of the network protocol, such as DELETE, PUT and GET with HTTP, should it be possible to manipulate a resource.
__2. Client-server based.__ There should be a clear delineation between the client and server. UI and request-gathering concerns are the client’s domain. Data access, workload management and security are the server’s domain. This loose coupling of the client and server enables each to be developed and enhanced independent of the other.
__3. Stateless operations.__ All client-server operations should be stateless, and any state management that is required should take place on the client, not the server.
__4. RESTful resource caching.__ All resources should allow caching unless explicitly indicated that caching is not possible.
__5. Layered system.__ REST allows for an architecture composed of multiple layers of servers.
__6. Code on demand.__ Most of the time, a server will send back static representations of resources in the form of XML or JSON. However, when necessary, servers can send executable code to the client.

## Requirements:
- Python 3.8
- Install Flask
- VSCode or Sublime Text, etc.
- Git
- SQL

## Content:
__Section 1 :__ First REST API
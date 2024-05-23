let backendUrl;
switch(process.env.NODE_ENV) {
  case 'production':
    backendUrl = 'https://production-backend-url/api/lyb/';
    break;
  case 'development':
    backendUrl = 'http://127.0.0.1:8080/api/lyb/';
    break;
  case 'uat':
    backendUrl = 'http://127.0.0.1:8090/api/lyb/';
    break;
  default:
    backendUrl = 'http://127.0.0.1:8088/api/lyb/';
}
export { backendUrl };
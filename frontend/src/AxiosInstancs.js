import axios from "axios";

const axiosApiInstance = axios.create();

axiosApiInstance.interceptors.request.use(async (config) => {
  try {
    const accessToken = localStorage.getItem("access_token");
    config.headers = {
      authorization: `Bearer ${accessToken}`,
    };
    return config;
  } catch (err) {
    console.log(err.response);
  }
});

axiosApiInstance.interceptors.response.use(
  (response) => {
    return response;
  },
  async (err) => {
    if (err.response.status === 422) {
      try {
        const res = await axios.post(
          "http://www.localhost:8000/users/refresh",
          {},
          {
            headers: {
              Authorization: `Bearer ${localStorage.getItem("refresh_token")}`,
            },
          }
        );
        localStorage.setItem("access_token", res.data.access_token);
      } catch (err) {
        console.log(err.response);
      }
    }
    return Promise.reject(err);
  }
);

export default axiosApiInstance;

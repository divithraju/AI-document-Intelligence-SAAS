import axios from "axios";


const API_URL = "http://localhost:8000/query";


export const queryDB = async (payload) => {
const res = await axios.post(API_URL, payload);
return res.data;
};

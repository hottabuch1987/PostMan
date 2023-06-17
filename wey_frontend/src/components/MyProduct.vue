<template>
<div class="p-4 bg-white border border-gray-200 rounded-lg">
        <h3 class="mb-6 text-xl">Мои товары</h3>

        <div class="space-y-4">
            <div class="flex items-center justify-between"
                v-for="product in products"
                :key="product.id"
            >
                <div class="flex items-center space-x-2">
                    <img :src="product.get_image" class="w-[40px] rounded-full">
                    
                    <p class="text-xs"><strong>{{product.name}}</strong>  {{product.price}}</p>
                    
                 
                </div>
                    
                <!-- <RouterLink :to="{name: 'profile', params: {id: user.id}}" class="py-2 px-3 bg-purple-600 text-white text-xs rounded-lg">Посмотреть</RouterLink> -->
            </div>

         

          
        </div>
    </div>
</template>
<script>
import axios from 'axios'

export default {
    name: 'MyProduct',
    data() {
        return {
            products: []
        }
    },
    mounted() {
        this.getFriendSuggestions()
    },
    methods: {
        getFriendSuggestions() {
            axios
                .get('/api/products/latest-products/')
                .then(response => {
                    this.products = response.data
                    console.log(response.data)
                })
                .catch(error => {
                    console.log('error', error)
                })
            }
    },

}
</script>

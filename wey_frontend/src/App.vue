<template>
    <NavBar />
    
    <main class="px-8 py-6 bg-gray-100">
        <RouterView />
    </main>
        
    <Footer />

    <Toast />
</template>

<script>
import Toast from '@/components/Toast.vue'
import Footer from '@/components/Footer.vue'
import NavBar from '@/components/NavBar.vue'

export default {
             
        components: {
            Toast,
            NavBar,
            Footer,
        },

        
    }
</script>

<style lang="scss">

main{
    background: rgb(2,0,36);
    background: linear-gradient(90deg, rgb(119, 113, 241) 0%, rgba(89, 17, 184, 0.234) 14%, rgba(0,212,255,1) 100%); 
}


</style>
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.DESKeySpec;
import java.nio.charset.StandardCharsets;

public class My_personal_key {
    public static void main(String[] args) throws Exception{
        SecretKeyFactory MykeyFactory = SecretKeyFactory.getInstance("DES");
        byte[] Mykey = "123456789".getBytes(StandardCharsets.UTF_8);
        DESKeySpec myMaterial = new DESKeySpec(Mykey);
        SecretKey myDESkey = MykeyFactory.generateSecret(myMaterial);



    }
}
